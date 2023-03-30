# This python files gives examples of using the sample() function
# sample will pick unique indexes from a sequence only once!
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Ango','Bob','Ango','Melinda','Bob','Adam','Juliet']
print(random.sample(names, 7))
# This will consider names[0] as different to names[2] even though they contain the same values
# sample() will return a list of unique indexes and doesn't verify if the elements are unique
