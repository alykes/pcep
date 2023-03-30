# This python files gives examples of using the choice() function
# choice allows duplicates to be returned from the list
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Ango','Bob','Jane','Melinda','Richard','Adam','Juliet']
some_text = 'ThisIsARandomPieceOfText'
tup_1 = (1, 2, 3, 4, 5, 6, 7, 8)
#dict_1 = {'ango': "A+", "Betty": "C-", "Troung": "B+", "Adam": "A-"} # WILL NOT WORK!!!

print(random.choice(numbers))
print(random.choice(names))
print(random.choice(some_text))
print(random.choice(tup_1))
#print(random.choice(dict_1)) # Dictionaries do not work!!!

# Note that the argument passed to choice can have many types

for i in range(10):
    print(random.choice(numbers), end="\t")   # Will return numbers and doesn't consider duplicates