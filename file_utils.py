import os
import csv

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

def save_dict_to_latex(dictionary, filename):
 # Initialize an empty string to store the generated document.
    doc = ''
    doc += "\\documentclass{article}\n\\begin{document}\n"
    # Loop through each key-value pair in the dictionary.
    for section_title, table_data in dictionary.items():
        # Add the section title to the document.
        doc += f'\\section*{{{section_title}}}\n\n'

        # Convert the table data into a LaTeX table.
        table = '\\begin{tabular}{|c|p{0.9\linewidth}|c|}\n'
        table+="\\hline\n"
        
        for i,row in enumerate(table_data):
            table+=f"{i}&{row[0]}&{row[1]}\\\\\n\\hline\n"
            
        table += '\\end{tabular}\n\n'

        # Add the table to the document.
        doc += table
    doc +='\\end{document}'
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

def save_list_of_lists_to_latex(list_of_lists, filename):
    
    latex_code=""
    for i,sublist in enumerate(list_of_lists):
        latex_code += f"\\begin{{frame}}{{Question {i+1}}}\n"
        latex_code += "\\begin{tabular}{ccp{0.9\linewidth}}\n"
        for tup in sublist:
            latex_code += f"{tup[0]} & {tup[1]} & {tup[2][0]} \\\\\n"
            latex_code += "\\hline\n"
        latex_code += "\\end{tabular}\n"
        latex_code += "\\end{frame}\n"
    with open (filename,'w') as file:
        file.write(latex_code)
    return None

def create_directory(directory_path):
    """
    Create a directory if it doesn't exist.

    Args:
        directory_path (str): The path of the directory to create.

    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

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
