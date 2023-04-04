num_one = []
for i in range (1, 101):
    num_one.append(i)

# The above can be rewritten in a list comprehension as follows:
num_two = [num for num in range(1,101)]                     # num is the control variable

# with an if statement
num_three = [nums for nums in range(1, 101) if nums % 3 != 0 ]

# This will print alternating 1's and 0's in a list
num_four = [0 if numbers % 2 == 0 else 1 for numbers in range(100)]

# Nested lists - make the following list
'''
[1,2,3,4,5]
[1,2,3,4,5]
[1,2,3,4,5]
[1,2,3,4,5]
'''
num_five = [[i for i in range(1, 6)] for j in range(5)]     # where [i for i in range(1, 6)] is the control variable