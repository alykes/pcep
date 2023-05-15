# An example of how to replace one of the attributes in the date object using the replace method
from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

d = d.replace(year=1980)
print(d)

d = d.replace(1975, 1, 1)
print(d)

