import os
import tempfile
from utils.latex_utils import save_answers_to_latex, save_questions_to_latex, add_prompt, subtract_prompt, multiply_prompt, sum_prompt,take_prompt, create_group_computation_slide, replace_latex_tag

def test_save_answers_to_latex():
    dictionary = {
        "Section 1": [
            ["1", "2", "Question 1"],
            ["3", "4", "Question 2"]
        ],
        "Section 2": [
            ["5", "6", "Question 3"],
            ["7", "8", "Question 4"]
        ]
    }
    filename = os.path.join(tempfile.gettempdir(), "answers.tex")

    save_answers_to_latex(dictionary, filename)

    with open(filename, 'r') as file:
        content = file.read()

    assert "\\section*{Section 1}" in content
    assert "1 & 2 & Question 1 \\\\" in content
    assert "3 & 4 & Question 2 \\\\" in content
    assert "\\section*{Section 2}" in content
    assert "5 & 6 & Question 3 \\\\" in content
    assert "7 & 8 & Question 4 \\\\" in content


def test_save_questions_to_latex():
    list_of_lists = [
        [("Question 1", "Answer 1")],
        [("Question 2", "Answer 2"), ("Question 3", "Answer 3")]
    ]

    result = save_questions_to_latex(list_of_lists)

    assert "\\begin{frame}{Question 1}" in result
    assert "\\begin{frame}{Question 2}" in result
    assert "\\begin{frame}{Question 3}" in result
    assert "\\end{tabular}" in result


def test_add_prompt():
    number = 5
    factor = 3

    prompt_1, prompt_2, updated_number = add_prompt(number, factor)

    assert prompt_1 == "To the number add 3"
    assert prompt_2 == "5 + 3 = 8"
    assert updated_number == 8


def test_subtract_prompt():
    number = 10
    factor = 4

    prompt_1, prompt_2, updated_number = subtract_prompt(number, factor)

    assert prompt_1 == "From the number subtract 4"
    assert prompt_2 == "10 - 4 = 6"
    assert updated_number == 6


def test_multiply_prompt():
    number = 2
    factor = 5

    prompt_1, prompt_2, updated_number = multiply_prompt(number, factor)

    assert prompt_1 == "Multiply the number by 5"
    assert prompt_2 == "2 * 5 = 10"
    assert updated_number == 10


def test_sum_prompt():
    number = 123

    prompt_1, prompt_2, updated_number = sum_prompt(number, None)

    assert prompt_1 == "Sum the digits of the number"
    assert prompt_2 == "1 + 2 + 3 = 6"
    assert updated_number == 6


def test_take_prompt():
    number = 987654321
    factor = 4

    prompt_1, prompt_2, updated_number = take_prompt(number, factor)

    assert prompt_1 == "Take the last 4 digits from the number"
    assert prompt_2 == "4321"
    assert updated_number == 4321


def test_create_group_computation_slide():
    json_data = {
        "group_computation": [
            ["add", 2],
            ["subtract", 3],
            ["multiply", 4]
        ],
        "group_count": 6
    }

    result = create_group_computation_slide(json_data)

    assert "\\begin{frame}{Group computation}" in result
    assert "\\begin{column}{0.5\\textwidth}" in result
    assert "\\begin{enumerate}" in result
    assert "\\end{enumerate}" in result


def test_replace_latex_tag():
    in_file_path = os.path.join(tempfile.gettempdir(), "input.tex")
    out_file_path = os.path.join(tempfile.gettempdir(), "output.tex")
    replacement = {
        "<tag1>": "replacement1",
        "<tag2>": "replacement2"
    }

    with open(in_file_path, 'w') as file:
        file.write("<tag1> and <tag2>")

    replace_latex_tag(in_file_path, out_file_path, replacement)

    with open(out_file_path, 'r') as file:
        content = file.read()

    assert "replacement1 and replacement2" == content
