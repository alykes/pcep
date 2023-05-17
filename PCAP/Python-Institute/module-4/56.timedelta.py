# An example showing how a timedelta object stores its values.
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

# Result:
# Days: 16
# Seconds: 10800
# Microseconds: 0


# Printing a timedelta object.
delta_two = timedelta(weeks=2, days=2, hours=3)
print(delta_two)

# Result:
# 16 days, 3:00:00