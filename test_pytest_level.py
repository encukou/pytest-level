import subprocess
import textwrap
import sys

import pytest


def run(args, **kwargs):
    kwargs.setdefault('check', True)
    return subprocess.run(args, **kwargs)


@pytest.fixture
def run_pytest(tmp_path):
    def _run_pytest(test_file_content, *args, should_fail=False, **kwargs):
        filename = tmp_path / 'test_a.py'
        filename.write_text(textwrap.dedent(test_file_content))
        args = [sys.executable, '-m', 'pytest', filename, *args]
        kwargs['check'] = True
        if should_fail:
            with pytest.raises(subprocess.CalledProcessError):
                subprocess.run(args, **kwargs)
        else:
            subprocess.run(args, **kwargs)
    return _run_pytest


def test_sanity_positive(run_pytest):
    run_pytest(
        """
            def test_yup():
                assert 1 + 1 == 2
        """
    )


def test_sanity_negative(run_pytest):
    run_pytest(
        """
            def test_nope():
                assert 1 + 1 == 0
        """,
        should_fail=True,
    )


def test_level_marker(run_pytest):
    run_pytest(
        """
            import pytest

            @pytest.mark.level(1)
            def test_basic_math():
                assert 1 + 1 == 2

            @pytest.mark.level(2)
            def test_intermediate_math():
                assert 10 / 2 == 5

            @pytest.mark.level(3)
            def test_complicated_math():
                assert 10 ** 3 == 1000
        """,
    )


TEST_FILE_CONTENT = """
    import pytest

    @pytest.mark.level(1)
    def test_1_ok():
        assert True

    @pytest.mark.level(2)
    def test_2_ok():
        assert True

    @pytest.mark.level(3)
    def test_3_fail():
        assert False

    @pytest.mark.level(3)
    def test_4_fail():
        assert False

    @pytest.mark.level(3)
    def test_5_ok():
        assert True
"""


def test_deselects_larger(run_pytest):
    """Tests marked with a larger level are deselected"""
    run_pytest(TEST_FILE_CONTENT, '--level', '2')


def test_selects_given(run_pytest):
    """Test with the given level is selected"""
    run_pytest(TEST_FILE_CONTENT, '--level', '3', should_fail=True)


def test_selects_previous(run_pytest):
    """Test with lower levels are selected"""
    run_pytest(TEST_FILE_CONTENT, '--level', '5', should_fail=True)
