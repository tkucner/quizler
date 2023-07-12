import random
import csv


def add_id_numbers(list_of_lists):
    for i in range(len(list_of_lists)):
        list_of_lists[i] = [i + 1] + list_of_lists[i]
    return list_of_lists


def generate_quiz(json_data):
    """
    Generate a quiz based on the provided JSON data.

    Args:
        json_data (dict): The JSON data containing configuration settings.

    Returns:
        tuple: A tuple containing a dictionary of groups and their assigned questions,
               and a list of tuples representing question slides.

    Raises:
        IndexError: If the number of columns in the questions input is incorrect.
    """
    group_ids = list("0123456789ABCDEF"[:json_data["group_count"]])

    questions_input = []
    questions_slides = []
    groups_questions = {item: [] for item in group_ids}

    csv_file = open(json_data['questions_list'], 'r', encoding='utf-8-sig')
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        questions_input.append(row)
    # Check if there are groups of questions or not
    if len(questions_input[0]) == 2:
        questions_input = add_id_numbers(questions_input)
    random.shuffle(questions_input)
    if json_data["two_column"] and json_data["group_count"] % 2 == 0:
        question_i = 0
        for no in range(json_data["questions_count"]):
            local_questions_slides = []
            local_group_ids = random.sample(group_ids, len(group_ids))
            for group_id in range(1, len(group_ids), 2):
                while (not groups_questions[local_group_ids[group_id]] == [] and any(questions_input[question_i][0] is q_id for q_id in groups_questions[local_group_ids[group_id]][:][0])) or (not groups_questions[local_group_ids[group_id - 1]] == [] and any(questions_input[question_i][0] is q_id for q_id in groups_questions[local_group_ids[group_id-1]][:][0])):

                    item_to_move = questions_input.pop(question_i)
                    questions_input.append(item_to_move)
                groups_questions[local_group_ids[group_id]].append(questions_input[question_i])
                groups_questions[local_group_ids[group_id - 1]].append(questions_input[question_i])
                local_questions_slides.append(
                    (local_group_ids[group_id], local_group_ids[group_id - 1], questions_input[question_i]))
                question_i += 1
            questions_slides.append(local_questions_slides)
    else:
        question_i=0
        for no in range(json_data["questions_count"]):
            local_questions_slides = []
            local_group_ids = random.sample(group_ids, len(group_ids))
            for group_id in range(1, len(group_ids)):

                while not groups_questions[local_group_ids[group_id]] == [] and any(questions_input[question_i][0] is q_id for q_id in groups_questions[local_group_ids[group_id]][:][0]):
                    item_to_move = \
                        questions_input.pop(question_i)
                    questions_input.append(item_to_move)
                groups_questions[local_group_ids[group_id]].append(questions_input[question_i])
                local_questions_slides.append((local_group_ids[group_id], questions_input[question_i]))
                question_i += 1
                questions_slides.append(local_questions_slides)

    return groups_questions, questions_slides


def answer_per_student(group_questions, students):
    """
    Add answers to each student based on their assigned group's questions.

    Args:
        group_questions (dict): A dictionary containing groups and their assigned questions.
        students (list): A list of student data.

    Returns:
        list: A list of students with answers appended.

    """
    for i in range(len(students)):
        group = students[i][3]
        questions_with_answers = group_questions[group]
        for question in questions_with_answers:
            students[i].append(question[2])
    return students


def remove_letters(input_string):
    """
    Remove letters from a string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The input string with letters removed.

    """
    input_string = str(input_string)
    return ''.join(c for c in input_string if not c.isalpha())


def fun_add(factor, number):
    """
    Add a factor to a number.

    Args:
        factor (int): The factor to add.
        number (int): The number to which the factor is added.

    Returns:
        int: The result of adding the factor to the number.

    """
    return number + factor


def fun_subtract(factor, number):
    """
    Subtract a factor from a number.

    Args:
        factor (int): The factor to subtract.
        number (int): The number from which the factor is subtracted.

    Returns:
        int: The result of subtracting the factor from the number.

    """
    return number - factor


def fun_multiply(factor, number):
    """
    Multiply a number by a factor.

    Args:
        factor (int): The factor to multiply.
        number (int): The number to be multiplied.

    Returns:
        int: The result of multiplying the number by the factor.

    """
    return number * factor


def fun_sum(_, number):
    """
    Calculate the sum of the digits in a number.

    Args:
        _ (int): Ignored.
        number (int): The number to calculate the sum of digits.

    Returns:
        int: The sum of the digits in the number.

    """
    total = 0
    for digit in str(number):
        total += int(digit)
    return total


def number_to_group(number, group_count):
    """
    Convert a number to a group identifier.

    Args:
        number (int): The number to be converted.
        group_count (int): The total number of groups.

    Returns:
        str: The group identifier corresponding to the number.

    """
    hex_digits = '0123456789ABCDEF'
    remainder = number % group_count
    hex_digit = hex_digits[remainder]
    return hex_digit


def fun_take(factor, number):
    """
    Extract the last `factor` digits from a number.

    Args:
        factor (int): The number of digits to take.
        number (int): The original number.

    Returns:
        int: The last `factor` digits of the number.

    """
    return int(str(number)[-factor:])


def compute_group(number, process, group_count):
    """
    Compute the group assignment for a given number.

    Args:
        number (str): The input number.
        process (list): A list of tuples representing the computation process.
                        Each tuple contains a function name and a value.
        group_count (int): The total number of groups.

    Returns:
        str: The group assignment for the number.

    """
    function_dictionary = {
        "add": fun_add,
        "subtract": fun_subtract,
        "multiply": fun_multiply,
        "sum": fun_sum,
        "take": fun_take
    }
    number = remove_letters(number)
    for fun, val in process:
        number = function_dictionary[fun](val, number)
    return number_to_group(number, group_count)
