
""""
This module's purpose is to clean a list of data by filtering out non-digit strings.

This module contains the filter_nondigits function, which processes a list of strings by removing any entries that contain non-digit characters. Before performing this check, the function removes any new-line characters ("/n") and then strings containing valid digits are converted into integers and stored in a new list, which gets returned.

It is recommended to implement this module first before proceeding with other tasks.

Functions: filter_nondigits (data_list: list[str]) -> list [int]
    filters a list of strings, keeping only valid digit strings which are then converted to integers.

To test this module, open a new terminal in VSCode by navigating to the "View" tab, and selecting terminal. When the terminal opens, select the "+" symbol to open a new terminal and run the following code: python test_cleaner.py 

"""

def filter_nondigits(data_list: list[str]) -> list[int]:
    """
    filters out all strings containing non-digit characters after removing new-line characters.
    Converts valid strings into integers and returns them in a new list.
    
    :param data_list: List of strings
    :return: List of integers
    """
    result = []

    for item in data_list:
        cleaned_item = item.strip() #removes new line and other leading/trailing spaces

        if cleaned_item.isdigit(): #check if it contains strictly digits
            result.append(int(cleaned_item)) # convert to integer and store

    return result



    



