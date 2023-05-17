import calendar

class MyCalendar(calendar.Calendar):
    def __init__(self):
        super().__init__()
        
    def count_weekday_in_year(self, year, weekday):
        self.year = year
        self. weekday = weekday
        counter = 0
        
        if weekday != 0:
            weekday -= 1
        
        for mnth in range(1,13):
            
            for data in c.monthdays2calendar(self.year, mnth):
                if data[self.weekday][0] != 0:
                    counter += 1
                    # print("yeah")
                # print(data)
                
        return counter


c = MyCalendar()
print(c.count_weekday_in_year(2019, 0))
