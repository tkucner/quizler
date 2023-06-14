import jsonschema
import json
import os

def find_schema(extension="schema.json"):
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                return file_path

def validate_json(json_file, schema_file):
    try:
        with open(schema_file) as fs:
            schema = json.load(fs)
        with open(json_file) as fd:
            json_data = json.load(fd)

        jsonschema.validate(json_data, schema)
    except jsonschema.ValidationError as e:
        print("Validation error: JSON file is not valid according to the JSON schema.")
        print(e)
    except FileNotFoundError as e:
        print("File not found error:", e)
    return json_data
