from jot.jot import Jot


def test_jot_json(temporary_json_file):
    jot = Jot(temporary_json_file)
    assert jot.get("box.name") == "rabbit"
    assert jot.get("box.content") == "🐇"


def test_jot_yaml(temporary_yaml_file):
    jot = Jot(temporary_yaml_file)
    assert jot.get("box.name") == "rabbit"
    assert jot.get("box.content") == "🐇"
