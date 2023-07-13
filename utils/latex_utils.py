def save_answers_to_latex(dictionary, filename):
    """
    Save a dictionary of table data to a LaTeX document.

    Args:
        dictionary (dict): A dictionary containing section titles as keys and table data as values.
        filename (str): The name of the output LaTeX file.

    """
    # Initialize an empty string to store the generated document.
    doc = ''
    doc += "\\documentclass{article}\n\\begin{document}\n"

    # Loop through each key-value pair in the dictionary.
    for section_title, table_data in dictionary.items():
        # Add the section title to the document.
        doc += f'\\section*{{{section_title}}}\n\n'

        # Convert the table data into a LaTeX table.
        table = '\\begin{tabular}{|c|c|p{0.9\\linewidth}|c|}\n'
        table += "\\hline\n"

        for i, row in enumerate(table_data):
            table += f"{i}&{row[0]}&{row[1]}&{row[2]}\\\\\n\\hline\n"

        table += '\\end{tabular}\n\n'

        # Add the table to the document.
        doc += table

    doc += '\\end{document}'

    # Save the generated document to a file.
    with open(filename, 'w') as file:
        file.write(doc)


def save_questions_to_latex(list_of_lists):
    """
    Generate LaTeX code for a list of questions.

    Args:
        list_of_lists (list): A list of lists, where each inner list represents a question.

    Returns:
        str: The generated LaTeX code.

    """
    latex_code = ""

    for i, sublist in enumerate(list_of_lists):
        latex_code += f"\\begin{{frame}}{{Question {i + 1}}}\n"

        if len(sublist[0]) == 2:
            latex_code += "\\begin{tabular}{cp{0.9\\linewidth}}\n"
        else:
            latex_code += "\\begin{tabular}{ccp{0.9\\linewidth}}\n"

        for tup in sublist:
            if len(tup) == 2:
                latex_code += f"{tup[0]} & {tup[1][1]} \\\\\n"
            else:
                latex_code += f"{tup[0]} & {tup[1]} & {tup[2][1]} \\\\\n"

            latex_code += "\\hline\n"

        latex_code += "\\end{tabular}\n"
        latex_code += "\\end{frame}\n"

    return latex_code


def add_prompt(number, factor):
    """
    Generate prompts for adding a factor to a number.

    Args:
        number (int): The number to which the factor will be added.
        factor (int): The factor to be added.

    Returns:
        tuple: A tuple containing the prompt strings and the updated number.

    """
    prompt_1 = "To the number add " + str(factor)
    prompt_2 = str(number) + " + " + str(factor) + " = " + str(number + factor)
    number = number + factor

    return prompt_1, prompt_2, number


def subtract_prompt(number, factor):
    """
    Generate prompts for subtracting a factor from a number.

    Args:
        number (int): The number from which the factor will be subtracted.
        factor (int): The factor to be subtracted.

    Returns:
        tuple: A tuple containing the prompt strings and the updated number.

    """
    prompt_1 = "From the number subtract " + str(factor)
    prompt_2 = str(number) + " - " + str(factor) + " = " + str(number - factor)
    number = number - factor

    return prompt_1, prompt_2, number


def multiply_prompt(number, factor):
    """
    Generate prompts for multiplying a number by a factor.

    Args:
        number (int): The number to be multiplied.
        factor (int): The factor by which the number will be multiplied.

    Returns:
        tuple: A tuple containing the prompt strings and the updated number.

    """
    prompt_1 = "Multiply the number by " + str(factor)
    prompt_2 = str(number) + " * " + str(factor) + " = " + str(number * factor)
    number = number * factor

    return prompt_1, prompt_2, number


def sum_prompt(number, _):
    """
    Generate prompts for summing the digits of a number.

    Args:
        number (int): The number whose digits will be summed.

    Returns:
        tuple: A tuple containing the prompt strings and the updated number.

    """
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
    """
    Generate prompts for taking the last 'factor' digits from a number.

    Args:
        number (int): The number from which the digits will be taken.
        factor (int): The number of digits to be taken.

    Returns:
        tuple: A tuple containing the prompt strings and the updated number.

    """
    prompt_1 = "Take the last " + str(factor) + " digits from the number"
    prompt_2 = str(number)[-factor:]
    number = int(str(number)[-factor:])

    return prompt_1, prompt_2, number


def create_group_computation_slide(json_data):
    """
    Create a group computation slide in LaTeX based on the given JSON data.

    Args:
        json_data (dict): A dictionary containing the data for group computation.

    Returns:
        str: The generated LaTeX code for the slide.

    """
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

    latex_code += "\\begin{frame}{Group computation}\n"
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
    Load a LaTeX file, replace specific tags with multiline LaTeX code,
    and save the modified content to a new file.

    Args:
        in_file_path (str): The path of the LaTeX file to load.
        out_file_path (str): The path of the output LaTeX file to create.
        replacement (dict): A dictionary containing the tags to replace as keys
                            and the corresponding multiline LaTeX code as values.

    """
    # Load the contents of the LaTeX file
    with open(in_file_path, 'r') as file:
        content = file.read()

    # Replace the tags with the replacement code
    for key, item in replacement.items():
        content = content.replace(key, item)

    # Save the modified content to a new file
    with open(out_file_path, 'w') as file:
        file.write(content)
