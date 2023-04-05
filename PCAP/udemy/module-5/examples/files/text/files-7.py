# Simply open, print the contents of the file one line at a time, counts the amount of lines and then closes the file
try:
    stream = open('animals.txt')

    lines = stream.readlines()

    print('This is the contents of the lines var:', lines)
    print('The number of lines in the file is:', len(lines))

    for line in lines:
        print(line, end='')

    stream.close()

except Exception as e:
    print('An error has occurred:', e)