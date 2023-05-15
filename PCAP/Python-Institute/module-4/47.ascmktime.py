import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))         # If no argument is provided to the asctime() function, then localtime() is used.
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

# Result: 
# Mon Nov  4 14:53:00 2019
# 1572879180.0