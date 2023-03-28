# factorial functions and recursion

# Iterative Approach
def get_factorial(number):
    for x in range(1, number + 1):
        factorial *= x
    return factorial

get_factorial(6)


def get_factorial_recursive(number):
    if number <= 1:
        return 1
    return number * get_factorial_recursive(number - 1) 

get_factorial_recursive(6)

# This is how the recursive function works
# get_factorial_recursive(6)=
#     6 * get_factorial_recursive(5)
#         5 * get_factorial_recursive(4)
#             4 * get_factorial_recursive(3)
#                 3 * get_factorial_recursive(2)
#                     2 * get_factorial_recursive(1)
#                         1
# 6 * 5 * 4 * 3 * 2 * 1
