year = int(input("Enter a year: "))
#
# Write your code here.
#	
if year >= 1582:
    if year % 4:
        print('common year - div 4')
    elif year % 100:
        print('leap year - div 100')
    elif year % 400:
        print('common year - div 400')
    else:
        print('Leap Year - All failed!')
else:
    print('Not within the Gregorian calendar period')