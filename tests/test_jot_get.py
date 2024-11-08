import pytest
from jot.jot import Jot

@pytest.mark.parametrize("temp_file_fixture", [
    "temporary_json_file",
    "temporary_yaml_file",
    "temporary_toml_file",
    "temporary_xml_file",
])
def test_jot_get_value(temp_file_fixture, request):
    temp_file_path = request.getfixturevalue(temp_file_fixture)
    jot = Jot(temp_file_path)
    assert jot.get("box.name") == "rabbit"
    assert jot.get("box.content") == "🐇"
