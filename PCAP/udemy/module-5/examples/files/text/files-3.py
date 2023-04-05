# Simply open, print the contents and then close a file
try:
    stream = open('animals.txt')

    print(stream.read(10))    # This reads the first 10 bytes of a file

    stream.close()

except Exception as e:
    print('An error has occurred:', e)