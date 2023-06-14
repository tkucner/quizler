import sys
import csv
import json
import os
from file_utils import save_array_as_csv, save_dict_to_file, save_list_of_lists_to_file, create_directory
from quiz_utils import generate_quiz, answer_per_student, compute_group, remove_letters
from validation_utils import find_schema, validate_json

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print("Usage: python quizler [<schema_file>] <json_file>")
    sys.exit(1)

schema_file = []
json_file = []

if len(sys.argv) == 2:
    schema_file = find_schema()
    json_file = sys.argv[1]

if len(sys.argv) == 3:
    schema_file = sys.argv[1]
    json_file = sys.argv[2]

json_data = validate_json(json_file, schema_file)
students = []

with open(json_data['students_list'], 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")

    # Read the contents of the CSV file into a list
    for row in csv_reader:
        students.append(row)

# Perform the mathematical operation on the third column of each row
for i in range(len(students)):
    value = students[i][2]

    result = compute_group(value, json_data['group_computation'], json_data['group_count'])
    students[i].append(str(result))

create_directory(json_data["name"])
file_name = "student_groups.csv"
file_path = os.path.join(json_data["name"], file_name)
save_array_as_csv(students, file_path)

groups_questions, questions_slides = generate_quiz(json_data)

file_name = "questions_in_groups.txt"
file_path = os.path.join(json_data["name"], file_name)
save_dict_to_file(groups_questions, file_path)

file_name = "questions_in_slides_raw.txt"
file_path = os.path.join(json_data["name"], file_name)
save_list_of_lists_to_file(questions_slides, file_path)

students_with_answers = answer_per_student(groups_questions, students)
file_name = "students_with_answers.csv"
file_path = os.path.join(json_data["name"], file_name)
save_array_as_csv(students_with_answers, file_path)
