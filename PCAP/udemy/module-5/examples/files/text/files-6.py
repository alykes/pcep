# Simply open, print the contents of the file line at a time, counts the amount of lines and then closes the file
try:
    stream = open('animals.txt')

    counter = 0

    line = stream.readline()      # This will read the file one line at a time.
    while line != '':
        print(line, end='-')
        line = stream.readline()
        counter += 1

    stream.close()

    print('\nThe number of lines in the file is:', counter)

except Exception as e:
    print('An error has occurred:', e)