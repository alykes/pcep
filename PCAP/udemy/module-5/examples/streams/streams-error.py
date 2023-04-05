from os import strerror
# Simply open and close a file
try:
    stream = open('nonexistant.txt')

    # Code goes here

    stream.close()

except Exception as e:
    
    print(strerror(e.errno))