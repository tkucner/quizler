import os
import csv
import shutil


def save_raw_answers_to_file(dictionary, filename):
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


def save_raw_questions_to_file(list_of_lists, filename):
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


