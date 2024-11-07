import jot.loader as ld
from tests.conftest import temporary_json_file, temporary_yaml_file,  TEMPLATE


def test_json_loader(temporary_json_file):
    loader = ld.JSONLoader(temporary_json_file)
    data = loader.load()
    expected_data = TEMPLATE
    assert data == expected_data


def test_factory_json_loader(temporary_json_file):
    loader = ld.FileLoaderFactory.get(temporary_json_file)
    actual_type = type(loader)
    expected_type = ld.JSONLoader
    assert actual_type is expected_type



def test_factory_yaml_loader(temporary_yaml_file):
    loader = ld.FileLoaderFactory.get(temporary_yaml_file)
    actual_type = type(loader)
    expected_type = ld.YAMLoader
    assert actual_type is expected_type


def test_yaml_loader(temporary_yaml_file):
    loader = ld.YAMLoader(temporary_yaml_file)
    data = loader.load()
    assert data == TEMPLATE
