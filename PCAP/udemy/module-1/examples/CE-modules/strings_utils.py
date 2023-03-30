import string_utils

def halve_strings(string_list):
    
    my_list = []

    for element in string_list:
        my_list.append(string_utils.halve_string(element))
    
    return (my_list)