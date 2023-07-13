import os
import csv
import shutil
from utils.file_utils import save_raw_answers_to_file, save_raw_questions_to_file, create_directory, initialise_directory


def test_save_raw_answers_to_file(tmp_path):
    dictionary = {
        "Group 1": ["Question 1", "Question 2"],
        "Group 2": ["Question 3", "Question 4"],
    }
    filename = os.path.join(tmp_path, "answers.txt")

    save_raw_answers_to_file(dictionary, filename)

    with open(filename, 'r') as file:
        content = file.read()

    assert content == "+++++++++++++++GROUP Group 1+++++++++++++++\nQuestion 1\nQuestion 2\n+++++++++++++++GROUP Group 2+++++++++++++++\nQuestion 3\nQuestion 4\n"


def test_save_raw_questions_to_file(tmp_path):
    list_of_lists = [
        ["Question 1", "Question 2"],
        ["Question 3", "Question 4"],
    ]
    filename = os.path.join(tmp_path, "questions.txt")

    save_raw_questions_to_file(list_of_lists, filename)

    with open(filename, 'r') as file:
        content = file.read()

    assert content == "++++++++++++++++SLIDE 0++++++++++++++++\nQuestion 1\nQuestion 2\n++++++++++++++++SLIDE 1++++++++++++++++\nQuestion 3\nQuestion 4\n"


def test_create_directory(tmp_path):
    directory_path = os.path.join(tmp_path, "new_directory")

    create_directory(directory_path)

    assert os.path.exists(directory_path)
    assert os.path.isdir(directory_path)


def test_initialise_directory(tmp_path):
    json_data = {
        "slide_template": "quiz_slides_template.tex",
        "name": "my_quiz",
    }
    directory_path = os.path.join(tmp_path, json_data["name"])
    template_path = os.path.join(directory_path, json_data["name"] + ".tex")

    initialise_directory(json_data)

    assert os.path.exists(directory_path)
    assert os.path.exists(template_path)


def test_save_array_as_csv(tmp_path):
    array = [
        ["1", "2", "3"],
        ["4", "5", "6"],
    ]
    file_path = os.path.join(tmp_path, "array.csv")

    save_array_as_csv(array, file_path)

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        rows = [row for row in reader]

    assert rows == [["1", "2", "3"], ["4", "5", "6"]]
