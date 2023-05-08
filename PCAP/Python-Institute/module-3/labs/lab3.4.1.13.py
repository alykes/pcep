# Add and subtract days from the current day of the week and return the result
class WeekDayError(Exception):
    pass
	

class Weeker:
    #
    dow_lst = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    #

    def __init__(self, day):
        #
        self.dow = day
        try: 
            self.day_num = Weeker.dow_lst.index(self.dow) 
        except:
            raise WeekDayError
        #

    def __str__(self):
        #
        return self.dow
        #

    def add_days(self, n):
        #

        self.dow_num = (n + self.day_num) % 7
        self.dow = Weeker.dow_lst[self.dow_num] 
        
        return self.dow
        #

    def subtract_days(self, n):
        #
        self.dow_num = (self.day_num - n + 1) % 7
        self.dow = Weeker.dow_lst[self.dow_num] 
        #


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
