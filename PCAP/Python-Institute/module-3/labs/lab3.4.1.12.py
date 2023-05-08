# Increment and decrement counter and return the timer reading
class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        #
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        #

    def __str__(self):
        #
        if self.hours < 10:
            str_hours = "0" + str(self.hours)
        else:
            str_hours = str(self.hours)
        if self.minutes < 10:
            str_minutes = "0" + str(self.minutes)
        else: 
            str_minutes = str(self.minutes)
        if self.hours < 10:
            str_seconds = "0" + str(self.seconds)
        else:
            str_seconds = str(self.seconds)
        
        
        return  str_hours + ":" + str_minutes + ":" + str_seconds
        

        #

    def next_second(self):
        #
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
        #

    def prev_second(self):
        #
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds = 59
            self.minutes -= 1
            if self.minutes == -1:
                self.minutes = 59
                self.hours -= 1
                if self.hours == -1:
                    self.hours = 23
        #


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
