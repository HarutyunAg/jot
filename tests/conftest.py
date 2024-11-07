import yaml
import json
import pytest
import tempfile
from pathlib import Path


TEMPLATE: dict = {
    "user": {
        "name": "Alice",
        "age": 30
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

    with tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode="w") as f:
        json.dump(TEMPLATE, f)
        f_path = f.name
    yield f_path
    Path(f_path).unlink()


@pytest.fixture
def temporary_yaml_file():
    """
    Fixture to create a temporary YAML file for testing.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".yaml", mode="w") as f:
        yaml.dump(TEMPLATE, f)
        f_path = f.name
    yield f_path
    Path(f_path).unlink()