# Some more examples of how to present the datetime, date and time objects in strings
# Refer to https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
from datetime import datetime, date, time

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

d = date(2019, 12, 5)
print(d.strftime("%d-%b-%Y"))