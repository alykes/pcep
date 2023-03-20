def unique(input_list=[]):
    return_list = []

    for element in input_list:
        if element not in return_list:
            return_list.append(element)
    
    return return_list

    
print(unique([1, 2, 3, 3, 3, 3, 4, 5]))
print(unique([]))
