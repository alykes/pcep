# Simply open, print the contents of the file 1 byte at a time and then close a file
try:
    stream = open('animals.txt')

    character = stream.read(1)      # This will read the file one character at a time.
    while character != '':
        print(character, end='-')
        character = stream.read(1)

    stream.close()

except Exception as e:
    print('An error has occurred:', e)