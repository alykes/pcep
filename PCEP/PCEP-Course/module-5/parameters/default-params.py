print('Yiasou', 'Malaka', end='.', sep='_' ) # end default is \n and spe default is a whitespace

def print_letter_count(text, letter='a'): # this sets the default value of letter to a (it can be overidden), this means you don't have to supply all arguments when invoking the function!
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
        print(char, end='')
    print('\nThe letter', letter, 'appears', counter, 'times.')

print_letter_count('How many a\'s are in this string?')

# NOTE: any parameters of a function with a default value must be defined at the end of the function definition
# All positional arguments must appear before any named arguments!
