# Demo on how to check if a year is a leap year
# and to also check how many days between certain years.
import calendar

print(calendar.isleap(2004))

print(calendar.leapdays(2004, 2005))  # Up to but not including 2005.
