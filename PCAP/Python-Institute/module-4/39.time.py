# Will get a timestamp of the current time (this is the amount of seconds that have passed since Unix Epoch - Jan 1 1970 at 00:00:00 UTC)
# Will convert that timestamp into a date
from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)