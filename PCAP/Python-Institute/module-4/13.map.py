# - build the list_1 with values from 0 to 4;
# - next, use map along with the first lambda to create a new list in which 
#   all elements have been evaluated as 2 raised to the power taken from the 
#   corresponding element from list_1;
# - list_2 is printed then;
# - in the next step, use the map() function again to make use of the generator 
#   it returns and to directly print all the values it delivers; as you can see, 
#   we've engaged the second lambda here - it just squares each element from list_2.

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
