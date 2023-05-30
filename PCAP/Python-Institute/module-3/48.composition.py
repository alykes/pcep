# This is an example of compositon. The subclass is treated like a container and passed to the Vehicle Super Class
# where is picks up the additional properties of the Vehicle class
# 
import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)


# Result: 
# wheels:  True True
# wheels:  True False
# tracks:  False True
# tracks:  False False