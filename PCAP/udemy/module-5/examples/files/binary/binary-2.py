try:
    bf = open('file.bin', 'rb') # open the binary file for reading.
    byte_array = bf.read()       # reads the entire file into the byte_array
    bf.close()                  # close the file
except Exception as e:
    print('An error occured:', e)

print(byte_array, '\n')

for byte in byte_array:
    print(hex(byte), end=' ')

print('\n')

for byte in byte_array:
    print(int(byte), end=' ')