import jsonschema
import json
import os


def find_schema(extension="schema.json"):
    """
    Find the schema file with the specified extension in the current directory and its subdirectories.

    Args:
        extension (str, optional): The file extension of the schema file. Defaults to "schema.json".

    Returns:
        str: The path to the schema file, or None if not found.
    """
    for root, dirs, files in os.walk('..'):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                return file_path
    return None


def validate_json(json_file, schema_file):
    """
    Validate a JSON file against a JSON schema.

    Args:
        json_file (str): The path to the JSON data file.
        schema_file (str): The path to the JSON schema file.

    Returns:
        dict: The parsed JSON data if validation is successful.

    Raises:
        jsonschema.ValidationError: If the JSON data is not valid according to the JSON schema.
        FileNotFoundError: If the JSON or schema file is not found.
    """
    try:
        # Load the JSON schema
        with open(schema_file) as fs:
            schema = json.load(fs)

        # Load the JSON data
        with open(json_file) as fd:
            json_data = json.load(fd)

        # Validate the JSON data against the schema
        jsonschema.validate(json_data, schema)
    except jsonschema.ValidationError as e:
        print("Validation error: JSON file is not valid according to the JSON schema.")
        print(e)
        raise
    except FileNotFoundError as e:
        print("File not found error:", e)
        raise
    return json_data
