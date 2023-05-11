# This is a method of using list comprehension in place, instead of saving the values to variables
for v in [1 if x % 2 == 0 else 0 for x in range(10)]:       # The list exists as a whole
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):       # There is no list, just subsequent values
    print(v, end=" ")
print()