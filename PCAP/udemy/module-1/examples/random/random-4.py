# This python files gives examples of using the sample() function
# sample will pick unique indexes from a sequence only once!
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Ango','Bob','Jane','Melinda','Richard','Adam','Juliet']
some_text = 'ThisIsARandomPieceOfText'
tup_1 = (1, 2, 3, 4, 5, 6, 7, 8)
#dict_1 = {'ango': "A+", "Betty": "C-", "Troung": "B+", "Adam": "A-"} # WILL NOT WORK!!!
#dict_2 = { 1: 'Ango', 2: 'Johnson', 3: 'Irini'}

print(random.sample(numbers, 5))
print(random.sample(names, 7))
print(random.sample(some_text, 2))
print(random.sample(tup_1, 4))
#print(random.sample(dict_1, 3)) # Dictionaries do not work!!!

# Note that the argument passed to sample can have many types