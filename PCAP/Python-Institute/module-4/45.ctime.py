# ctime takes a timestamp argument and returns the date as a string
# Mon Nov  4 14:53:00 2019  <--- In this format
import time

timestamp = 1572879180
print(time.ctime(timestamp))


# returns the current timestamp
print(time.time())

# Converts the current time to a string with the date and time, e.g., 'Mon May 22 01:54:57 2023'
print(time.ctime())

