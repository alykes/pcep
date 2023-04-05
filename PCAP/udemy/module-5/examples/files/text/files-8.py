# Simply open, print the contents of the file 2 bytes at a time and then closes the file
# this behaves a little strangely, so take note of this example.
try:
    stream = open('animals.txt')

    lines = stream.readlines(2)

    while len(lines) != 0:
        for line in lines:
            print(line, sep='')
            print(lines)

        print('Read the next 2 bytes')
        lines = stream.readlines(2)

    stream.close()

except Exception as e:
    print('An error has occurred:', e)