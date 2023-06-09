import os
import sys
import jsonschema
import json
import csv

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def save_array_as_csv(array, file_path):
    # Create the directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Save the array as a CSV file
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(array)



def remove_letters(input_string):
    input_string=str(input_string)
    return ''.join(c for c in input_string if not c.isalpha())

def fun_add(factor,number):
    return number+factor

def fun_substract(factor,number):
    return number-factor

def fun_multiply(factor,number):
    return number*factor

def fun_sum(_,number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

def number_to_group(number,group_count):
    hex_digits = '0123456789ABCDEF'
    remainder = number % group_count
    hex_digit = hex_digits[remainder]
    return hex_digit

def fun_take(factor,number):
    return int(str(number)[-factor:])

def compute_group(number,process,group_count):
    function_dictionary={
        "add":fun_add,
        "substract":fun_substract,
        "multiply":fun_multiply,
        "sum":fun_sum,
        "take":fun_take
    }
    number=remove_letters(number)
    for fun,val in process:
        number=function_dictionary[fun](val,number)
    return number_to_group(number,group_count)



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
students=[]
with open(json_data['students_list'], 'r',encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=";")

    # Read the contents of the CSV file into a list
    for row in csv_reader:
        students.append(row)

# Perform the mathematical operation on the third column of each row
for i in range(len(students)):
    value = students[i][2]

    result = compute_group(value,json_data['group_computation'],json_data['group_count'])
    students[i].append(str(result))

create_directory(json_data["name"])
file_name = "student_groups.csv"
file_path = os.path.join(json_data["name"], file_name)

save_array_as_csv(students, file_path)

