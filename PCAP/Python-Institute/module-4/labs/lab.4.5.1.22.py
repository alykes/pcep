from datetime import datetime, date, time, timedelta

dt = datetime(2020, 11, 4, 14, 53 ,00)

print(dt)
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Weekday: %w"))
print(dt.strftime("Day of the year: %j"))
print(dt.strftime("Week number of the year: %W"))


# Result
# 2020-11-04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44