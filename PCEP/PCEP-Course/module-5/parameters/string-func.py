# multiple parameters
def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
        print(char, end='')
    print('\nThe letter', letter, 'appears', counter, 'times.')

print_letter_count('The quick brown fox jumps over the lazy dog', 'e') # positional arguments

print_letter_count( letter='e', text='The quick brown fox jumps over the lazy dog') # named arguments can be placed in any order
