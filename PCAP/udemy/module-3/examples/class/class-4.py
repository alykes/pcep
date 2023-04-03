class Car():
    def __init__(self, model, colour, initial_speed = 0):   # Classes also allow you to set derfault values
        self.model = model
        self.colour = colour
        if initial_speed < 0:
            self.__speed = 0
        else:
            self.__speed = initial_speed

    def speed_up(self):
        self.__speed += 5
    
    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        print('Current __speed is:', self.__speed)
        
my_car = Car('Ford','Red')

my_car.speed_up()
my_car.speed_up()
my_car.show_speed()

my_car.speed = -100
my_car.show_speed()     # result will be 0 as the previous line won't be able to set the speed