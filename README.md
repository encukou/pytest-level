# pytest-level

Mark test cases with a *level*, then de-select tests with a given level or higher.

When giving a teaching/practice assignment with pre-written tests, either all
tests can be given at once (leaving students overwhelmed and unsure which
failures should be fixed next), or piece-wise (in individual files -- which
becomes a mess for larger projects).

With this plugin, tests for a teaching/practice assignment can be given in
a single file. Students are then told to run with `--level 1`, fix the few red
tests, then go to `--level 2`, etc.
Unlike with keywords, all the lower-level tests will still be run:
`--level 2` will run both `level(1)` and `level(2)` tests.


## Installation

In a Python environment (e.g. `venv`), do:

    python -m pip install pytest-level


## Usage

Mark tests with a numeric `level` marker:

    @pytest.mark.level(1)
    def test_basic_math():
        assert 1 + 1 == 2

    @pytest.mark.level(2)
    def test_intermediate_math():
        assert 10 / 2 == 5

    @pytest.mark.level(3)
    def test_complicated_math():
        assert 10 ** 3 == 1000

Then, run pytest with `--level`:

    python -m pytest --level 2

This will deselect tests of a higher level.

Without `--level`, all tests are run.


## Licence

The code is available under a MIT license. May it serve you well.
