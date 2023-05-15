# An example of creating a time object. Also not that all the parameters are optional.  
from datetime import time

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
print("tzinfo:", t.tzinfo)
print("fold:", t.fold)