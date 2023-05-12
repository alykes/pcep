# This will create a bytearray and then assign it some values in the same manner as writing to a list.  
data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))