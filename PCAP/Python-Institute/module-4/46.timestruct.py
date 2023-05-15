# converts a timestamp to gm time and localtime. 
# for gmtime(), the isdst attribute is always 0
import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))
