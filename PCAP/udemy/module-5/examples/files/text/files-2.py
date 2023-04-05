# Simply open, print the contents and then close a file
try:
    stream = open('animals.txt')

    print(stream.read())    # This reads the entire file

    stream.close()

except Exception as e:
    print('An error has occurred:', e)