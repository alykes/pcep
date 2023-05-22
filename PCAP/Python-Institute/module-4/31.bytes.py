# Creates a bytearray and then writes it to a binary file
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Reads from the stream 5 bytes at a time...note that this doesn't read the entire contents, you need a loop for that.

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


