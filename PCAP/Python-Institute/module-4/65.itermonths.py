# The code displays all days in November 2019. 
# Because the first day of November 2019 was a Friday, 
# the following days are also returned to get the complete week: 10/28/2019 (Monday) 10/29/2019 (Tuesday) 10/30/2019 (Wednesday) 10/31/2019 (Thursday).
# The last day of November 2019 was a Saturday, so in order to keep the complete week, one more day is returned 12/01/2019 (Sunday).
import calendar  

c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end="\n")
