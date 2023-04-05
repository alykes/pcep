# In this situation you don't need to close the stream!!!!
# This works because stream is an iterable object
try:
    stream = open('animals.txt')
    for line in stream:
        print(line, end = '')
except Exception as e:
    print('An error occured: ', e)
