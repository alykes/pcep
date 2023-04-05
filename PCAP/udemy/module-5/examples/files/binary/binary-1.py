data = bytearray(100)   # Creates an array with 100 bytes and each one is set to 0
data[0] = 100           # This will store the first byte of the bytearray to the binary representation of 100

data[1] = 120

try:
    stream = open('file.bin', 'wb') # open the file as a writable binary file.
    stream.write(data)
    stream.close()
except Exception as e:
    print('An error occured:', e)