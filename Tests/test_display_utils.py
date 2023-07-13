from utils.display_utils import print_raw_answers, print_raw_questions


def test_print_raw_answers(capsys):
    dictionary = {
        "Group 1": ["Question 1", "Question 2"],
        "Group 2": ["Question 3", "Question 4"],
    }

    print_raw_answers(dictionary)

    captured = capsys.readouterr()
    output_lines = captured.out.split("\n")

    assert output_lines[0] == "+++++++++++++++GROUP Group 1+++++++++++++++"
    assert output_lines[1] == "Question 1"
    assert output_lines[2] == "Question 2"
    assert output_lines[3] == "+++++++++++++++GROUP Group 2+++++++++++++++"
    assert output_lines[4] == "Question 3"
    assert output_lines[5] == "Question 4"


def test_print_raw_questions(capsys):
    list_of_lists = [
        ["Question 1", "Question 2"],
        ["Question 3", "Question 4"],
    ]

    print_raw_questions(list_of_lists)

    captured = capsys.readouterr()
    output_lines = captured.out.split("\n")

    assert output_lines[0] == "++++++++++++++++SLIDE 0++++++++++++++++"
    assert output_lines[1] == "Question 1"
    assert output_lines[2] == "Question 2"
    assert output_lines[3] == "++++++++++++++++SLIDE 1++++++++++++++++"
    assert output_lines[4] == "Question 3"
    assert output_lines[5] == "Question 4"
