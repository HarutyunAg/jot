import jot.loader as ld
from tests.conftest import TEMPLATE


def test_json_loader_loads_data_correctly(temporary_json_file):
    loader = ld.JSONLoader(temporary_json_file)
    data = loader.load()
    assert data == TEMPLATE


def test_yaml_loader_loads_data_correctly(temporary_yaml_file):
    loader = ld.YAMLoader(temporary_yaml_file)
    data = loader.load()
    assert data == TEMPLATE


def test_toml_loader_loads_data_correctly(temporary_toml_file):
    loader = ld.TOMLLoader(temporary_toml_file)
    data = loader.load()
    assert data == TEMPLATE


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
    

def test_factory_toml_loader(temporary_toml_file):
    loader = ld.FileLoaderFactory.get(temporary_toml_file)
    actual_type = type(loader)
    expected_type = ld.TOMLLoader
    assert actual_type is expected_type
