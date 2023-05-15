# Examples of how datetime is represented.
from datetime import datetime

print("today:", datetime.today())       # tzinfo set to None
print("now:", datetime.now())           # same as above unless you pass tz argument
print("utcnow:", datetime.utcnow())     # tzinfo set to None, returns UTC
print()
