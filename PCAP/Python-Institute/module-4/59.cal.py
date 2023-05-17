# Prints a calendar for the month of that year
# The month function requires two positional arguments (theyear, themonth)
# These functions also take two arguments:
#   w – date column width (default 2)
#   l – number of lines per week (default 1)

import calendar
print(calendar.month(2020, 11))

# The function below will print the calendar without requiring the print() function
calendar.prmonth(1980, 1)