input_numbers = [5.0, 3.5, 7.8, 9.9, 10.0]

# Single parameter
def get_average(input_numbers):
    sum = 0.0
    for i in input_numbers:
        sum += i
    average = sum / len(input_numbers)
    print(average)

get_average(input_numbers) # passing arguments

get_average([5.0, 3.5, 7.8, 9.9, 10.0]) # passing arguments
