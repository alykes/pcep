# Returns the 
import calendar  

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")            # Returns the number of the day in the month, 0 if it's not in the day

print()

for iter in c.itermonthdays2(2019, 11):
    print(iter, end=" ")            # Returns tuples consisting of a day of the month number and a week day number 

print()

for iter in c.itermonthdays3(2019, 11):
    print(iter, end=" ")            # Returns tuples consisting of a year, a month, and a day of the month numbers.

print()    

for iter in c.itermonthdays4(2019, 11):
    print(iter, end=" ")            # Returns tuples consisting of a year, a month, a day of the month, and a day of the week numbers.
