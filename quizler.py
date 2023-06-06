import os
import sys
import jsonschema
import json

def find_schema(extension="schema.json"):
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                return file_path
            

def validate_json( json_file,schema_file):
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


if len(sys.argv) == 1 or len(sys.argv)>3:
    print("Usage: python quizler [<schema_file>] <json_file>")
    sys.exit(1)

schema_file=[]
json_file=[]

if len(sys.argv) == 2:
    schema_file=find_schema()
    json_file=sys.argv[1]

if len(sys.argv) == 3:
    schema_file=sys.argv[1]
    json_file=sys.argv[2]

json_data=validate_json(json_file,schema_file)
print(json_data)

