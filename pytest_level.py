import pytest

def pytest_addoption(parser):
    parser.addoption('--level', type=int)


@pytest.fixture
def level(config):
    return config.getoption('--level')


def pytest_collection_modifyitems(session, config, items):
    selected_level = config.getoption('--level')
    if selected_level == None:
        return

    deselected_items = set()
    for item in items:
        for marker in item.iter_markers('level'):
            [marker_level] = marker.args
            if marker_level > selected_level:
                deselected_items.add(item)
    selected_items = [item for item in items if item not in deselected_items]
    items[:] = selected_items
    config.hook.pytest_deselected(items=deselected_items)
