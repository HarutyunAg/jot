from jot.loader import JSONLoader, YAMLoader, TOMLLoader, XMLLoader, FileLoaderFactory
from tests.conftest import TEMPLATE
import pytest

@pytest.mark.parametrize("loader_class, temp_file_fixture", [
    (JSONLoader, "temporary_json_file"),
    (YAMLoader, "temporary_yaml_file"),
    (TOMLLoader, "temporary_toml_file"),
])
def test_loader_loads_data_correctly(loader_class, temp_file_fixture, request):
    temp_file_path = request.getfixturevalue(temp_file_fixture)
    loader = loader_class(temp_file_path)
    data = loader.load()
    assert data == TEMPLATE


@pytest.mark.parametrize("temp_file_fixture, expected_loader_type", [
    ("temporary_json_file", JSONLoader),
    ("temporary_yaml_file", YAMLoader),
    ("temporary_toml_file", TOMLLoader),
    ("temporary_xml_file", XMLLoader),
])
def test_factory_creates_correct_loader(temp_file_fixture, expected_loader_type, request):
    temp_file_path = request.getfixturevalue(temp_file_fixture)
    loader = FileLoaderFactory.get(temp_file_path)
    assert isinstance(loader, expected_loader_type)
