import random
import csv
from utils.quiz_utils import add_id_numbers, generate_quiz, answer_per_student, remove_letters, fun_add, fun_subtract, fun_multiply, fun_sum, fun_take, number_to_group, compute_group
def test_add_id_numbers():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = add_id_numbers(matrix)
    assert result == [[1, 1, 2, 3], [2, 4, 5, 6], [3, 7, 8, 9]]


# def test_generate_quiz():
#     json_data = {
#         "group_count": 3,
#         "questions_list": "questions.csv",
#         "two_column": False,
#         "questions_count": 6
#     }
#     result = generate_quiz(json_data)
#     groups_questions, questions_slides = result
#     assert len(groups_questions) == 3
#     assert len(questions_slides) == 6


# def test_answer_per_student():
#     group_questions = {
#         "A": [[1, "Question 1", "Answer 1"], [2, "Question 2", "Answer 2"]],
#         "B": [[3, "Question 3", "Answer 3"]],
#         "C": [[4, "Question 4", "Answer 4"]]
#     }
#     students = [
#         ["John", "Doe", "john.doe@example.com", "A"],
#         ["Jane", "Smith", "jane.smith@example.com", "B"],
#         ["Bob", "Johnson", "bob.johnson@example.com", "C"]
#     ]
#     result = answer_per_student(group_questions, students)
#     assert len(result) == 3
#     assert len(result[0]) == 5
#     assert len(result[1]) == 5
#     assert len(result[2]) == 5


def test_remove_letters():
    input_string = "abc123def456"
    result = remove_letters(input_string)
    assert result == "123456"


def test_fun_add():
    factor = 3
    number = 5
    result = fun_add(factor, number)
    assert result == 8


def test_fun_subtract():
    factor = 4
    number = 10
    result = fun_subtract(factor, number)
    assert result == 6


def test_fun_multiply():
    factor = 5
    number = 2
    result = fun_multiply(factor, number)
    assert result == 10


def test_fun_sum():
    number = 123
    result = fun_sum(None, number)
    assert result == 6


def test_number_to_group():
    number = 5
    group_count = 3
    result = number_to_group(number, group_count)
    assert result in ["2", "5", "8"]


def test_fun_take():
    factor = 4
    number = 987654321
    result = fun_take(factor, number)
    assert result == 4321


# def test_compute_group():
#     number = "31415"
#     process = [("add", 2), ("subtract", 3), ("multiply", 4), ("sum", None), ("take", 2)]
#     group_count = 6
#     result = compute_group(number, process, group_count)
#     assert result in ["2", "5", "8"]
