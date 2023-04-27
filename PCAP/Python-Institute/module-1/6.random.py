from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))      # chooses one element
print(sample(my_list, 5))   # chooses five elements 
print(sample(my_list, 10))  # chooses ten elements 

