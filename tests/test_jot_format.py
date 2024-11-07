from jot.jot import Jot


def test_format_existing_keys(temporary_json_file):
    jot = Jot(temporary_json_file)
    input_string = "Hello {user.name}, welcome to the {box.name} box with {box.content}!"
    expected_output = "Hello Alice, welcome to the rabbit box with 🐇!"
    assert jot.format(input_string) == expected_output


def test_format_missing_key(temporary_json_file):
    jot = Jot(temporary_json_file)
    input_string = "Hello {user.name}, your favorite animal is {user.favorite_animal}!"
    expected_output = "Hello Alice, your favorite animal is {user.favorite_animal}!"
    assert jot.format(input_string) == expected_output


def test_format_multiple_placeholders(temporary_json_file):
    jot = Jot(temporary_json_file)
    input_string = "{user.name} is {user.age} years old and loves {box.content}. Missing: {box.color}"
    expected_output = "Alice is 30 years old and loves 🐇. Missing: {box.color}"
    assert jot.format(input_string) == expected_output


def test_format_empty_input(temporary_json_file):
    jot = Jot(temporary_json_file)
    input_string = ""
    expected_output = ""
    assert jot.format(input_string) == expected_output


def test_format_no_placeholders(temporary_json_file):
    jot = Jot(temporary_json_file)
    input_string = "No placeholders here!"
    expected_output = "No placeholders here!"
    assert jot.format(input_string) == expected_output
