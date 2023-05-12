# Creates a bytearray, populates it and then writes it to a file
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

# This section reads the binary file and prints it out to the stdout
from os import strerror

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())     # Reads the entire contents of the file and places it in a bytearray of the same size!
                                    # be cautious with this type of approach as you could potentially create a bytearray size larger than you computer memory.
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

