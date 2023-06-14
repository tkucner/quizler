import random
import csv

def generate_quiz(json_data):
    group_ids = list("0123456789ABCDEF"[:json_data["group_count"]])
    
    questions_input = []
    questions_slides = []
    groups_questions = {item: [] for item in group_ids}
    
    csv_file = open(json_data['questions_list'], 'r', encoding='utf-8-sig')
    csv_reader = csv.reader(csv_file, delimiter=";")

    # Read the contents of the CSV file into a list
    for row in csv_reader:
        questions_input.append(row)
    random.shuffle(questions_input)

    # Check if there are groups of questions or not
    if len(questions_input[0]) == 3:
        pass
    elif len(questions_input[0]) == 2:
        if json_data["two_column"] and json_data["group_count"] % 2 == 0:
            question_i = 0
            for no in range(json_data["questions_count"]):
                local_questions_slides = []
                local_group_ids = random.sample(group_ids, len(group_ids))
                for group_id in range(1, len(group_ids), 2):
                    while ((not groups_questions[local_group_ids[group_id]] == []) and (questions_input[question_i] in groups_questions[local_group_ids[group_id]])) or ((not groups_questions[local_group_ids[group_id-1]] == []) and (questions_input[question_i] in groups_questions[local_group_ids[group_id-1]])):
                        item_to_move = questions_input.pop(questions_input[question_i])  
                        questions_input.append(item_to_move)
                    groups_questions[local_group_ids[group_id]].append(questions_input[question_i])
                    groups_questions[local_group_ids[group_id-1]].append(questions_input[question_i])
                    local_questions_slides.append((local_group_ids[group_id], local_group_ids[group_id-1], questions_input[question_i]))
                    question_i += 1
                questions_slides.append(local_questions_slides)
        else:
            pass
            
    else:
        print("Something is wrong, too many columns")
    return groups_questions, questions_slides

def answer_per_student(group_questions, students):
    for i in range(len(students)):
        group = students[i][3]
        questions_with_answers = group_questions[group]
        for question in questions_with_answers:
            students[i].append(question[1])
    return students

def remove_letters(input_string):
    input_string = str(input_string)
    return ''.join(c for c in input_string if not c.isalpha())

def fun_add(factor, number):
    return number + factor

def fun_subtract(factor, number):
    return number - factor

def fun_multiply(factor, number):
    return number * factor

def fun_sum(_, number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

def number_to_group(number, group_count):
    hex_digits = '0123456789ABCDEF'
    remainder = number % group_count
    hex_digit = hex_digits[remainder]
    return hex_digit

def fun_take(factor, number):
    return int(str(number)[-factor:])

def compute_group(number, process, group_count):
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
