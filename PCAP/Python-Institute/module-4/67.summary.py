# Put all the examples in one place for datetime and time
import datetime
import time

now = time.time()
print(".time.time() - timestamp from Unix Epoch:", now)
print(".fromtimestamp(TIMESTAMP):", datetime.date.fromtimestamp(now))

today = datetime.date.today()
print(".today():", today)
print(".weekday():", today.weekday())
print(".isoweekday():", today.isoweekday())

isodate = datetime.date.fromisoformat('2023-05-22')
print(".fromisoformat('DATE'):", isodate)


t = datetime.time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
print("tzinfo:", t.tzinfo)
print("fold:", t.fold)

print("Sleeping for 5 seconds")
time.sleep(5)

# Convert the current time to a string with date and time information, e.g., Mon May 22 01:54:57 2023
print("ctime():\t", time.ctime())           # convert time to a string - takes a timestamp as an argument
print("ctime(now):\t", time.ctime(now))     # convert time to a string - takes a timestamp as an argument
print("gmtime():\t", time.gmtime())         # returns a struct_time object - takes a timestamp as an argument
print("localtime():\t", time.localtime())   # returns a struct_time object - takes a timestamp as an argument
print("asctime:\t", time.asctime())         # Convert a struct_time to an ascii date string "Day Month Date Hour:Minute:Second Year", if no tuple provided, uses localtime()
print("mktime:\t", time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))     # Make a timestamp from the struct time object provided

print(".today():", today)
today = today.replace(year=2030)
print(".replace(year=2030)", today)

# datetime object
dt_today = datetime.datetime.today()
print("today:\t", dt_today)
dt_now = datetime.datetime.now()
print("now:\t", dt_now)
dt_utcnow = datetime.datetime.utcnow()
print("utcnow:\t", dt_utcnow)

print("datetime:", dt_today)
print("datetime.time():", dt_today.time())
print("datetime.date():", dt_today.date())

dt_value = datetime.datetime(2024, 4, 20, 16, 20)   # You can also assign a date and time to a datetime object

# Directives are used to format datetime and date values into characters that you can format.
t = datetime.time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime.datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

d = datetime.date(2019, 12, 5)
print(d.strftime("%d-%b-%Y"))

# Directives can also be used on the time module
# strftime() can also take a timestamp as the second value
d2 = time.localtime()       # This creates a time_struct object
print(time.strftime("%d %b %Y", d2))

#strptime() can be used on time and datetime objects
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))                # returns a time_struct object
print(datetime.datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))   # returns a datetime object

# Performing calculations on datetime and dates
d1 = datetime.date.today()
d2 = datetime.date(2000, 1, 1)
print(d1 - d2)

dt1 = datetime.datetime.now()
dt2 = datetime.datetime(2000, 1, 1, 0, 0)
print(dt1 - dt2)

# timedelta
d1 = datetime.timedelta(weeks=10, days=4)
d2 = datetime.timedelta(weeks=8, days=1)

d3 = d1 - d2
print(d3)
print(d3.days, d3.seconds, d3.microseconds)     # a timedelta object only keeps these values, even though you can specify days, seconds, microseconds, milliseconds, minutes, hours, weeks.
print(d1 - d2)


############# CALENDAR #############

import calendar

# TextCalendar
cal_text = calendar.TextCalendar()
print(cal_text.formatmonth(2023, 5))
cal_text.setfirstweekday(calendar.WEDNESDAY)
print(cal_text.formatmonth(2023, 5))

# Creating a calendar
cal = calendar.calendar(2023, w=3, c=2, m=4)
print(cal)

# Creating Calendar object, think of this as a class to iterate through values
cal_obj = calendar.Calendar(firstweekday=0) #Create a calendar object with Monday as the first day in the week.
for day in cal_obj.iterweekdays():
    print(day)

print()

cal_obj.setfirstweekday(calendar.SUNDAY)
for day in cal_obj.iterweekdays():
    print(day)

for month in cal_obj.itermonthdates(2023, 5):
    print(month)