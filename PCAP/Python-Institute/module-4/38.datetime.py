# Get the current date and print out the results.
from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# Create a date object; you must provide the year, month and day
my_date = date(2019, 11, 4)
print(my_date)