import jsonschema
import json
import os
from utils.validation_utils import find_schema, validate_json

def test_find_schema():
    schema_path = find_schema()
    assert schema_path is not None
    assert os.path.isfile(schema_path)


def test_validate_json():
    json_file = "data.json"
    schema_file = "schema.json"

    # Create a valid JSON data file
    data = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }
    with open(json_file, "w") as f:
        json.dump(data, f)

    # Create a valid JSON schema file
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "email": {"type": "string", "format": "email"}
        },
        "required": ["name", "age", "email"]
    }
    with open(schema_file, "w") as f:
        json.dump(schema, f)

    # Test validation with valid JSON data
    result = validate_json(json_file, schema_file)
    assert result == data

    # Test validation with invalid JSON data
    invalid_data = {
        "name": "Jane Smith",
        "age": "30",
        "email": "jane.smith@example.com"
    }
    with open(json_file, "w") as f:
        json.dump(invalid_data, f)

    try:
        validate_json(json_file, schema_file)
        assert False, "Validation should raise jsonschema.ValidationError"
    except jsonschema.ValidationError:
        pass

    # Clean up the files
    os.remove(json_file)
    os.remove(schema_file)
