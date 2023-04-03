class House():
    counter = 0

    def __init__(self, address, area, price):
        self.address = address
        self.area = area
        self.price = price

        House.quality = 'Low'   # Class Variable - Can be accessed outside the class definition 
        self.quality = 'Medium' # Instance Variable - Can be accessed outside the class definition 
        quality = 'High'        # Local Variabele - CANNOT be access outside the class definition

        print('Class Variable:', House.quality, 'Instance Variable:', self.quality, 'Local Variable', quality)     # This will work without issue

    def present(self):
        print('The house at', self.address, 'is in the area of', self.area, 'and costs', self.price)
    

my_place = House('1 Bravo St, Broville', 'The Bros', '$500,000')

my_place.present()

print('Class Variable:', House.quality)    # This will work
print('Instance Variable:', my_place.quality)     # This will work
# print(quality)         # This will not work