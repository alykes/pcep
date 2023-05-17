from datetime import date
from datetime import datetime

# Creating a timedelta object by using calculations based on date objects
d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

# Creating a timedelta object by using calculations based on datetime objects
dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)
