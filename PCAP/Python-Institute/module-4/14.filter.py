from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]                      # Generates a list of random integers between -10 and 10
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))   # Passes the list (data) to the lambda and if the condition is TRUE, will then append that to the `filtered` list

print(data)
print(filtered)
