import yaml
import json
import toml
import pytest
import tempfile
from pathlib import Path


TEMPLATE: dict = {
    "user": {
        "name": "Alice",
        "age": 16
    },

    "box": {
        "name": "rabbit",
        "content": "🐇"
    }
}


@pytest.fixture
def temporary_json_file():
    """
    Fixture to create a temporary JSON file for testing.
    """

    with tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode="w", encoding="utf-8") as f:
        json.dump(TEMPLATE, f)
        f_path = f.name
    yield f_path
    Path(f_path).unlink()


@pytest.fixture
def temporary_yaml_file():
    """
    Fixture to create a temporary YAML file for testing.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".yaml", mode="w", encoding="utf-8") as f:
        yaml.dump(TEMPLATE, f)
        f_path = f.name
    yield f_path
    Path(f_path).unlink()


@pytest.fixture
def temporary_toml_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix=".toml", mode="w", encoding="utf-8") as f:
        toml.dump(TEMPLATE, f)
        f_path = f.name
    yield f_path
    Path(f_path).unlink()


@pytest.fixture
def temporary_xml_file():
    content = """<?xml version="1.0"?>
    <root>
        <user>
            <name>Alice</name>
            <age>30</age>
        </user>
        <box>
            <name>rabbit</name>
            <content>🐇</content>
        </box>
    </root>
    """
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml", mode="w", encoding="utf-8") as f:
        f.write(content)
        f_path = f.name
    yield f_path
    Path(f_path).unlink()
