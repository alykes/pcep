class Car():
    def __init__(self, model, colour, initial_speed = 0):   # Classes also allow you to set derfault values
        self.model = model
        self.colour = colour
        if initial_speed < 0:
            self.speed = 0
        else:
            self.speed = initial_speed

    def speed_up(self):
        self.speed += 5
    
    def slow_down(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def show_speed(self):
        print('Current Speed is:', self.speed)
        
my_car = Car('Ford','Red')

my_car.speed_up()
my_car.speed_up()
my_car.show_speed()


## This code still allows a user to set the speed directly

my_car.speed = -100
my_car.show_speed()     # result will be -100
# look at class-4.py for the proper way to handle this