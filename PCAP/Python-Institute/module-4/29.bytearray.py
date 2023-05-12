# Creating a byte array and then writing it to a binary file
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)          # this method also returns the number of successfully written bytes
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Reading the binary file.
data = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data)       # Notice that to read the data, we use a special method readinto()
                            # Also note that it doesn't create a new bytearray object but fills an already existing one
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


