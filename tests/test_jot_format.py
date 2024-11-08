import pytest
from jot.jot import Jot

format_test_cases = [
    # Test cases with existing keys
    ("Hello {user.name}! {box.content}", "Hello Alice! 🐇"),
    # Test case with a missing key
    ("Hello {user.name}, your favorite animal is {user.favorite_animal}!",
     "Hello Alice, your favorite animal is {user.favorite_animal}!"),
    # Test case with multiple placeholders, including a missing one
    ("{user.name} is {user.age} years old and loves {box.content}. Missing: {box.color}",
     "Alice is 16 years old and loves 🐇. Missing: {box.color}"),
    # Test case with empty input
    ("", ""),
    # Test case with no placeholders
    ("No placeholders here!", "No placeholders here!")
]

@pytest.mark.parametrize("temp_file_fixture, input_string, expected_output", [
    (temp_file, input_string, expected_output)
    for temp_file in ["temporary_json_file",
                      "temporary_yaml_file",
                      "temporary_toml_file",
                      "temporary_xml_file"]
    for input_string, expected_output in format_test_cases
])
def test_jot_formatting(temp_file_fixture, input_string, expected_output, request):
    temp_file = request.getfixturevalue(temp_file_fixture)
    jot = Jot(temp_file)
    formatted = jot.format(input_string)
    assert formatted == expected_output, f"{formatted}--- NOT ---{expected_output}"
