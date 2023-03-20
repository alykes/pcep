input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

# Single parameter
def get_average(input_numbers):
    sum = 0.0
    for i in input_numbers:
        sum += i
    average = sum / len(input_numbers)
    return average # exits the function immediately

avg = get_average(input_numbers) # passing arguments

if avg > 5.0:
    print('The average is way too high!')


# Return
def is_first_last_equal(number_list):
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False

print(is_first_last_equal([10, 20, 30, 20, 10])) # result True
print(is_first_last_equal([10, 20, 30, 20, 100])) # result False

print(is_first_last_equal([])) # Index error as it is an empty list

## Check for empty list and return straight out of the function!
def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return
    
    if (number_list[0] == number_list[-1]):
        return True
    else:
        return False

print(is_first_last_equal([])) # Will return the value of None
