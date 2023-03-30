import math

def halve_string(input_string):
    mid = math.ceil(len(input_string)/2) 
    return (input_string[:mid], input_string[mid:])