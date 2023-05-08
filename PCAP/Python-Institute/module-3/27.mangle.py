class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")


obj = Classy()
obj.visible()           # This is a perfectly fine call to the visible() method.

try:
    obj.__hidden()      # This will return an error as the method is hidden and can't be accessed like this.
except:
    print("failed")

obj._Classy__hidden()   # You can still call a hidden function via the mangled name.

