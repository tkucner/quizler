from utils.display_utils import print_raw_answers


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
