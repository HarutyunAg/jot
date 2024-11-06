import json
import pytest
from pathlib import Path
import jot.loader as ld

JSON_PATH = 'tests\\deps\\test.json'


def test_json_loader():
    loader = ld.JSONLoader(JSON_PATH)
    data = loader.load()
    expected_data = {
        "test_str": "testo", 
        "box": {
            "something": "🐇"
            }
        }
    assert data == expected_data


def test_factory_json_loader():
    loader = ld.FileLoaderFactory.get(JSON_PATH)
    actual_type = type(loader)
    expected_type = ld.JSONLoader
    assert actual_type is expected_type
