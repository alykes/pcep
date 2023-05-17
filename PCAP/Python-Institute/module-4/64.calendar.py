import calendar  

# Creates the calendar object with the week starting on Sunday (6)
c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
