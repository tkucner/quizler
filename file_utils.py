import os
import csv

def print_dict(dictionary, indent=0):
    for key, value in dictionary.items():
        print("+++++++++++++++GROUP {}+++++++++++++++".format(key))
        for question in value:
            print(question)

def save_dict_to_file(dictionary, filename):
    with open(filename, 'w') as file:
        for key, value in dictionary.items():
            file.write("+++++++++++++++GROUP {}+++++++++++++++\n".format(key))
            for question in value:
                file.write("{}\n".format(question))

def print_list_of_lists(list_of_lists):
    for i, inner_list in enumerate(list_of_lists):
        print("++++++++++++++++SLIDE {}++++++++++++++++".format(i))
        for inner_item in inner_list:
            print(inner_item)
        
def save_list_of_lists_to_file(list_of_lists, filename):
    with open(filename, 'w') as file:
        for i, inner_list in enumerate(list_of_lists):
            file.write("++++++++++++++++SLIDE {}++++++++++++++++\n".format(i))
            for inner_item in inner_list:
                file.write("{}\n".format(inner_item))

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

def save_array_as_csv(array, file_path):
    # Create the directory if it doesn't exist
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Save the array as a CSV file
    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(array)
