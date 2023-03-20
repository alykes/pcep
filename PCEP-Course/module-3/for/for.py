# Iterating through a string
for letter in 'Yiasou Malaka':
    print('Current Letter:', letter)


# This goes from 1 to 10 (start is inclusive and stop value is exclusive)
for number in range(1,11):
    print('Current number:',number)
print('Done')

# This goes from 0 to 10, default start value is always zero
for number in range(11):
    print('Current number using a single range value is:', number)
print('Done')

# This example uses a step counter
for number in range(1,11, 2):
    print('Current number:',number)
print('Done')