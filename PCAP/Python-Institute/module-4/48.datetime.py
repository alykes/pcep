#Create a datetime object and then return separate portions of the portion.  
from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)      # Datetime: 2019-11-04 14:53:00 - Creates the datetime object
print("Date:", dt.date())   # Date: 2019-11-04 - Returns the date portion of the object
print("Time:", dt.time())   # Time: 14:53:00 - Returns the time portion of the object


