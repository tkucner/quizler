import os
import csv
import shutil


def print_dict(dictionary):
    """
    Print the contents of a dictionary in a formatted manner.

    Args:
        dictionary (dict): The dictionary to print.

    """
    for key, value in dictionary.items():
        print("+++++++++++++++GROUP {}+++++++++++++++".format(key))
        for question in value:
            print(question)


def save_dict_to_file(dictionary, filename):
    """
    Save the contents of a dictionary to a file.

    Args:
        dictionary (dict): The dictionary to save.
        filename (str): The name of the file to save the dictionary to.

    """
    with open(filename, 'w') as file:
        for key, value in dictionary.items():
            file.write("+++++++++++++++GROUP {}+++++++++++++++\n".format(key))
            for question in value:
                file.write("{}\n".format(question))


def save_answers_to_latex(dictionary, filename):
    # Initialize an empty string to store the generated document.
    doc = ''
    doc += "\\documentclass{article}\n\\begin{document}\n"
    # Loop through each key-value pair in the dictionary.
    for section_title, table_data in dictionary.items():
        # Add the section title to the document.
        doc += f'\\section*{{{section_title}}}\n\n'

        # Convert the table data into a LaTeX table.
        table = '\\begin{tabular}{|c|p{0.9\\linewidth}|c|}\n'
        table += "\\hline\n"

        for i, row in enumerate(table_data):
            table += f"{i}&{row[0]}&{row[1]}\\\\\n\\hline\n"

        table += '\\end{tabular}\n\n'

        # Add the table to the document.
        doc += table
    doc += '\\end{document}'
    with open(filename, 'w') as file:
        file.write(doc)


def print_list_of_lists(list_of_lists):
    """
    Print the contents of a list of lists in a formatted manner.

    Args:
        list_of_lists (list): The list of lists to print.

    """
    for i, inner_list in enumerate(list_of_lists):
        print("++++++++++++++++SLIDE {}++++++++++++++++".format(i))
        for inner_item in inner_list:
            print(inner_item)


def save_list_of_lists_to_file(list_of_lists, filename):
    """
    Save the contents of a list of lists to a file.

    Args:
        list_of_lists (list): The list of lists to save.
        filename (str): The name of the file to save the list of lists to.

    """
    with open(filename, 'w') as file:
        for i, inner_list in enumerate(list_of_lists):
            file.write("++++++++++++++++SLIDE {}++++++++++++++++\n".format(i))
            for inner_item in inner_list:
                file.write("{}\n".format(inner_item))


def save_questions_to_latex(list_of_lists):
    latex_code = ""
    for i, sublist in enumerate(list_of_lists):
        latex_code += f"\\begin{{frame}}{{Question {i + 1}}}\n"
        latex_code += "\\begin{tabular}{ccp{0.9\\linewidth}}\n"
        for tup in sublist:
            latex_code += f"{tup[0]} & {tup[1]} & {tup[2][0]} \\\\\n"
            latex_code += "\\hline\n"
        latex_code += "\\end{tabular}\n"
        latex_code += "\\end{frame}\n"
    return latex_code


def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.

    Args:
        directory_path (str): The path of the directory to create.

    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def initialise_directory(json_data):
    shutil.copy(json_data["slide_template"], os.path.join(json_data["name"], json_data["name"] + ".tex"))


def save_array_as_csv(array, file_path):
    """
    Save a 2D array as a CSV file.

    Args:
        array (list): The 2D array to save.
        file_path (str): The path of the CSV file to save the array to.

    """
    # Create the directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the array as a CSV file
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(array)


def add_prompt(number, factor):
    prompt_1 = "To the number add " + str(factor)

    prompt_2 = str(number) + " + " + str(factor) + " = " + str(number + factor)
    number = number + factor
    return prompt_1, prompt_2, number


def subtract_prompt(number, factor):
    prompt_1 = "From the number substract " + str(factor)
    prompt_2 = str(number) + " - " + str(factor) + " = " + str(number - factor)
    number = number - factor
    return prompt_1, prompt_2, number


def multiply_prompt(number, factor):
    prompt_1 = "Multiply the number by " + str(factor)
    prompt_2 = str(number) + " * " + str(factor) + " = " + str(number * factor)
    number = number * factor
    return prompt_1, prompt_2, number


def sum_prompt(number, _):
    prompt_1 = "Sum the digits of the number"
    sum_of_digits = 0
    prompt_2 = ""
    first = True
    for digit in str(number):
        if first:
            prompt_2 = prompt_2 + digit
            first = False
            sum_of_digits += int(digit)
        else:
            prompt_2 = prompt_2 + " + " + digit
            sum_of_digits += int(digit)
    prompt_2 = prompt_2 + " = " + str(sum_of_digits)
    number = sum_of_digits
    return prompt_1, prompt_2, number


def take_prompt(number, factor):
    prompt_1 = "Take last " + str(factor) + " digits from the number"
    prompt_2 = str(number)[-factor:]
    number = int(str(number)[-factor:])
    return prompt_1, prompt_2, number


def create_group_computation_slide(json_data):
    latex_code = ""
    hex_digits = '0123456789ABCDEF'
    group_table = ""
    function_dictionary = {
        "add": add_prompt,
        "subtract": subtract_prompt,
        "multiply": multiply_prompt,
        "sum": sum_prompt,
        "take": take_prompt
    }
    latex_code += "\\begin{frame}{Gropup compuation}\n"
    latex_code += "\\begin{columns}\n"
    latex_code += "\\begin{column}{0.5\\textwidth}\n"
    latex_code += "\\begin{enumerate}\n"
    i = 1
    number = 31415926
    column_1 = ""
    column_2 = ""
    column_1 += "\\item<" + str(i) + "-> Take your student number\n"
    column_2 += "\\item<" + str(i) + "->" + str(number) + "\n"

    for key, item in json_data["group_computation"]:
        i += 1
        prompt_1, prompt_2, number = function_dictionary[key](number, item)
        column_1 += "\\item<" + str(i) + "->" + prompt_1 + "\n"
        column_2 += "\\item<" + str(i) + "->" + prompt_2 + "\n"
    i += 1
    column_1 += "\\item<" + str(i) + "->Modulo " + str(json_data["group_count"]) + "\n"
    column_2 += "\\item<" + str(i) + "->" + str(number) + "\\%" + str(json_data["group_count"]) + " =" + str(
        number % json_data["group_count"]) + "\n"
    number = number % json_data["group_count"]
    if json_data["group_count"] > 10:
        i += 1
        column_1 += "\\item<" + str(i) + "->Convert " + str(number) + " to group id.\n"
        column_2 += "\\item<" + str(i) + "->" + str(hex_digits[number]) + "\n"
        group_table += "\\only<" + str(i) + ">{\n"
        group_table += "\\begin{table}[]\n\\begin{tabular}{@{}"
        for _ in range(json_data["group_count"]):
            group_table += "c"
        group_table += "@{}}\n"
        group_table += "\\toprule\n"
        for i in range(json_data["group_count"]):

            group_table += str(i)
            if i < json_data["group_count"] - 1:
                group_table += "&"

        group_table += "\\\\\n"
        group_table += "\\midrule\n"
        for i in range(json_data["group_count"]):

            group_table += str(hex_digits[i])
            if i < json_data["group_count"] - 1:
                group_table += "&"

        group_table += "\\\\\n"
        group_table += "\\bottomrule\n \\end{tabular}\n\\end{table}\n}\n"
    latex_code += column_1
    latex_code += "\\end{enumerate}\n"
    latex_code += "\\end{column}\n"
    latex_code += "\\begin{column}{0.5\\textwidth}\n"
    latex_code += "\\begin{enumerate}\n"
    latex_code += column_2
    latex_code += "\\end{enumerate}\n"
    latex_code += "\\end{column}\n"
    latex_code += "\\end{columns}\n"
    if group_table != "":
        latex_code += group_table
    latex_code += "\\end{frame}"
    return latex_code


def replace_latex_tag(in_file_path, out_file_path, replacement):
    """
    Load a LaTeX file, replace a specific tag with multiline LaTeX code,
    and save the modified content to a new file.

    Args:
        in_file_path (str): The path of the LaTeX file to load.
        tag (str): The tag to replace.
        replacement (dict): The multiline LaTeX code to replace the tag with.
        :param out_file_path:

    """
    # Load the contents of the LaTeX file
    with open(in_file_path, 'r') as file:
        content = file.read()

    # Replace the tag with the replacement code
    for key, item in replacement.items():
        print(key, item)
        content = content.replace(key, item)

    # modified_content = content.replace(tag, replacement)

    # Save the modified content to a new file
    with open(out_file_path, 'w') as file:
        file.write(content)
