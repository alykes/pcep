# Simply open, print the contents of the file 1 byte at a time, counts the amount of characters and then closes the file
try:
    stream = open('animals.txt')

    counter = 0

    character = stream.read(1)      # This will read the file one character at a time.
    while character != '':
        print(character, end='-')
        character = stream.read(1)
        counter += 1

    stream.close()

    print('\nThe number of characters in the file is:', counter)

except Exception as e:
    print('An error has occurred:', e)