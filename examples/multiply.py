def multiply_values(some_list):
  multiplied_values = []

  for item in some_list:
    multiplied_values.append(item * 2)

  return multiplied_values

print(multiply_values([1, 2, 3]))