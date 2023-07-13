def print_raw_answers(dictionary):
    """
    Print the contents of a dictionary in a formatted manner.

    Args:
        dictionary (dict): The dictionary to print.

    """
    for key, value in dictionary.items():
        print("+++++++++++++++GROUP {}+++++++++++++++".format(key))
        for question in value:
            print(question)


def print_raw_questions(list_of_lists):
    """
    Print the contents of a list of lists in a formatted manner.

    Args:
        list_of_lists (list): The list of lists to print.

    """
    for i, inner_list in enumerate(list_of_lists):
        print("++++++++++++++++SLIDE {}++++++++++++++++".format(i))
        for inner_item in inner_list:
            print(inner_item)
