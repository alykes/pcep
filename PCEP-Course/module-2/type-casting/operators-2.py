# uniary and binary operators
# +12 = 12 and -5 = -5

# Order of operators
# 1. **
# 2. * / // %
# 3. + -
# Example: 2 + 3 * 2 = 8 and (2 + 3) * 2 = 10

# Approximation for floats
# print(0.1) = 0.1
# print(0.1 + 0.1 + 0.1) = 0.30000000000000004 Notice that it is not exactly 0.3 (this is because of the way the PC stores floats using binary and is onl;y a good approximation at best)

# Using powers - Python goes from the right to the left [RIGHT SIDED BINDING] all other operators are left sided bound!
# 2 ** 2 ** 3 
# Result is 256
# Breaking it down
# 2 ** 3 = 8 
# 2 ** 8 = 256