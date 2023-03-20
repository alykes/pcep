#The bitwise operators are:
# & 
# | 
# ~ 
# ^ 
# << 
# >>

first_bit = 1
second_bit = 0 

# AND
print(first_bit & second_bit)
# result 0

# OR
print(first_bit | second_bit)
# result 1

#XOR = when they are both different it returns 1
print(first_bit ^ second_bit)
# result 1

#logical negation   ~x = -x -1
print(~2)
# result -3

#bit shift Left
print(12 << 1)
# result 001100 shifting left means 011000 therefore 16 + 8 = 24
print(12 << 2)
# result 0001100 shifting left means 0110000 therefore 32 + 16 = 48

#bit shift right
print(12 >> 1)
# result 01100 shifting right means 00110 therefore 4 + 2 = 6
print(12 >> 2)
# result 01100 shifting right means 00011 therefore 2 + 1 = 3