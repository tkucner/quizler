import os
import sys
import jsonschema
import json
import csv
import random

def print_dict(dictionary, indent=0):
    for key, value in dictionary.items():
        print("+++++++++++++++GROUP {}+++++++++++++++".format(key))
        for question in value:
            print(question)

def save_dict_to_file(dictionary, filename):
    with open(filename, 'w') as file:
        for key, value in dictionary.items():
            file.write("+++++++++++++++GROUP {}+++++++++++++++\n".format(key))
            for question in value:
                file.write("{}\n".format(question))

def print_list_of_lists(list_of_lists):
    for i, inner_list in enumerate(list_of_lists):
        print("++++++++++++++++SLIDE {}++++++++++++++++".format(i))
        for inner_item in inner_list:
            print(inner_item)
        
def save_list_of_lists_to_file(list_of_lists, filename):
    with open(filename, 'w') as file:
        for i, inner_list in enumerate(list_of_lists):
            file.write("++++++++++++++++SLIDE {}++++++++++++++++\n".format(i))
            for inner_item in inner_list:
                file.write("{}\n".format(inner_item))


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

def generate_quiz(json_data):
    group_ids=list("0123456789ABCDEF"[:json_data["group_count"]])
    
    questions_input=[]
    questions_slides=[]
    groups_questions=my_dict = {item: [] for item in group_ids}
    
    csv_file= open(json_data['questions_list'], 'r',encoding='utf-8-sig')
    csv_reader = csv.reader(csv_file,delimiter=";")

    # Read the contents of the CSV file into a list
    for row in csv_reader:
        questions_input.append(row)
    random.shuffle(questions_input)

    # check if there are groups of questiosn or not
    if len(questions_input[0])==3:
        pass
    elif len(questions_input[0])==2:
        if(json_data["two_column"] and json_data["group_count"]%2==0):
            question_i=0
            for no in range(json_data["questions_count"]):
                local_questions_slides=[]
                local_group_ids=random.sample(group_ids,len(group_ids))
                for group_id in range(1,len(group_ids),2):
                    while ((not groups_questions[local_group_ids[group_id]] == []) and (questions_input[question_i] in groups_questions[local_group_ids[group_id]])) or ((not groups_questions[local_group_ids[group_id-1]] == []) and (questions_input[question_i] in groups_questions[local_group_ids[group_id-1]])):
                        item_to_move = questions_input.pop(questions_input[question_i])  
                        questions_input.append(item_to_move)
                    groups_questions[local_group_ids[group_id]].append(questions_input[question_i])
                    groups_questions[local_group_ids[group_id-1]].append(questions_input[question_i])
                    local_questions_slides.append((local_group_ids[group_id],local_group_ids[group_id-1],questions_input[question_i]))
                    question_i=question_i+1
                questions_slides.append(local_questions_slides)
            print_list_of_lists(questions_slides)
            print_dict(groups_questions)
        else:
            pass
            
    else:
        print("Somethign is wrong, too many columns")
    return groups_questions, questions_slides

def answer_per_student(group_questions,students):
    for i in range(len(students)):
        group=students[i][3]
        questions_with_answers=group_questions[group]

        for question in questions_with_answers:
            print(len(question))
            print(question)
            for q in question:
                print(q)
            students[i].append(question[1])
    return students
    


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

groups_questions, questions_slides=generate_quiz(json_data)

file_name = "questions_in_groups.txt"
file_path = os.path.join(json_data["name"], file_name)
save_dict_to_file(groups_questions, file_path)

file_name = "questions_in_slides_raw.txt"
file_path = os.path.join(json_data["name"], file_name)
save_list_of_lists_to_file(questions_slides, file_path)

students_with_answers=answer_per_student(groups_questions,students)
file_name = "students with asnwers.csv"
file_path = os.path.join(json_data["name"], file_name)
save_array_as_csv(students_with_answers, file_path)


