# An example of how to print the calendar to the screen.
import calendar

print(calendar.calendar(2023, m=4))

# This will print the calendar without having to invoke the print() function
# Also note that prcal also accepts the same parameters as calendar
calendar.prcal(2020)


# The parameters are:
# w – date column width (default 2)
# l – number of lines per week (default 1)
# c – number of spaces between month columns (default 6)
# m – number of columns (default 3)