# Simply open and close a file
try:
    stream = open('animals.txt')

    # Code goes here

    stream.close()

except Exception as e:
    print('An error has occurred:', e)