numbers = [1, 2, 3, 4]



numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

# List comprehension which does the exact same thing as the line above
numbers = [i for i in range(1, 101)]
print(numbers)

#Same as above example of but adds a condition
numbers = [i for i in range(1, 101) if i % 3 != 0 ]
print(numbers)