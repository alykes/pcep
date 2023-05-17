# Print the day of the week with the amount of letters specified
import calendar
print(calendar.weekheader(2))

print(calendar.weekheader(3))

calendar.setfirstweekday(6)                 # This line and the one below are the exact same line of code.
calendar.setfirstweekday(calendar.SUNDAY)   # calendar.SUNDAY is a constant and this line of code is equivalent to the one above

print(calendar.weekheader(2))