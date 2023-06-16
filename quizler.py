import sys
import os
import csv
from file_utils import save_array_as_csv, save_dict_to_file, save_list_of_lists_to_file, create_directory, \
    save_questions_to_latex, save_answers_to_latex, create_group_computation_slide, initialise_directory, \
    replace_latex_tag
from quiz_utils import generate_quiz, answer_per_student, compute_group
from validation_utils import find_schema, validate_json


def main(schema_file, json_file):
    """
    Main function to execute the quizler program.

    Args:
        schema_file (str): Path to the JSON schema file.
        json_file (str): Path to the JSON data file.
    """
    # Validate the JSON data using the provided schema file
    json_data = validate_json(json_file, schema_file)

    # Read the students list from the CSV file
    students = read_students_list(json_data['students_list'])

    # Calculate the groups for each student
    calculate_groups(students, json_data)

    # Create a directory for the quiz results
    create_directory(json_data["name"])
    initialise_directory(json_data)

    # Save the student groups as a CSV file
    save_array_as_csv(students, os.path.join(json_data["name"], "student_groups.csv"))

    # Generate the quiz questions and slides
    groups_questions, questions_slides = generate_quiz(json_data)

    # Save the questions grouped by IDs to a text file
    save_dict_to_file(groups_questions, os.path.join(json_data["name"], "questions_in_groups.txt"))
    save_answers_to_latex(groups_questions, os.path.join(json_data["name"], "questions_in_groups.tex"))

    # Save the questions grouped by slides to a text file
    save_list_of_lists_to_file(questions_slides, os.path.join(json_data["name"], "questions_in_slides_raw.txt"))
    questions_slides = save_questions_to_latex(questions_slides)

    # Assign answers to each student based on their group questions
    students_with_answers = answer_per_student(groups_questions, students)

    # Save the students with their answers as a CSV file
    save_array_as_csv(students_with_answers, os.path.join(json_data["name"], "students_with_answers.csv"))

    # Create group computation slides for LaTeX
    group_computation_slides = create_group_computation_slide(json_data)

    # Replace tags in the LaTeX template with generated content
    fill_in = {"%%GROUP_COMPUTATION%%": group_computation_slides,
               "%%QUESTIONS%%": questions_slides}
    replace_latex_tag("quiz_slides_template.tex", os.path.join(json_data["name"], json_data["name"] + ".tex"),
                      fill_in)


def read_students_list(students_list_file):
    """
    Read the students' information from the CSV file.

    Args:
        students_list_file (str): Path to the CSV file containing the students' information.

    Returns:
        list: A list of lists representing the students' information.
    """
    students = []
    with open(students_list_file, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        for row in csv_reader:
            students.append(row)
    return students


def calculate_groups(students, json_data):
    """
    Calculate the group for each student based on the provided computation and group count.

    Args:
        students (list): A list of lists representing the students' information.
        json_data (dict): Parsed JSON data containing the computation and group count.
    """
    for i in range(len(students)):
        value = students[i][2]
        result = compute_group(value, json_data['group_computation'], json_data['group_count'])
        students[i].append(str(result))


if __name__ == "__main__":
    # Check the command-line arguments
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print("Usage: python quizler [<schema_file>] <json_file>")
        sys.exit(1)

    schema_file = []
    json_file = []

    # Determine the schema and JSON file paths
    if len(sys.argv) == 2:
        schema_file = find_schema()
        json_file = sys.argv[1]

    if len(sys.argv) == 3:
        schema_file = sys.argv[1]
        json_file = sys.argv[2]

    # Call the main function
    main(schema_file, json_file)
