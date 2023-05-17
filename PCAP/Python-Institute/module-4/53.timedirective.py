# An example of the strftime function in the time module.
# Note that if you don't provide the second argument, the CURRENT time and date are used!

import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))   # Will format the provided date and time provided by the st variable.
print(time.strftime("%Y/%m/%d %H:%M:%S"))       # Will use the current date and time as no second argument is provided.
