# An example of some operations that can be performed on a timedelta object.
# Some of these include multiplication and addition.
from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print("delta:\t", delta)

delta2 = delta * 2
print("delta_2:", delta2)

d = date(2019, 10, 4) + delta2
print("d:\t", d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print("dt:\t", dt)
