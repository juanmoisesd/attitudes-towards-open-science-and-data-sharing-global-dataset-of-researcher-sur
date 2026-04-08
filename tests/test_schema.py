import json
import os
import pytest

def test_schema_file_exists():
    assert os.path.exists("schema.json")

def test_schema_is_valid_json():
    with open("schema.json", "r") as f:
        schema = json.load(f)
        assert schema["title"] == "Attitudes towards Open Science Dataset Schema"

def test_data_dictionary_exists():
    assert os.path.exists("data_dictionary.csv")
