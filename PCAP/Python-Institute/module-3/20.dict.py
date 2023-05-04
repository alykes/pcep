class Sample:
    gamma = 0 # Class variable.
    def __init__(self):
        self.alpha = 1 # Instance variable.
        self.__delta = 3 # Private instance variable.


obj = Sample()
obj.beta = 2  # Another instance variable (existing only inside the "obj" instance.)
print(obj.__dict__)

# Output: {'alpha': 1, '_Sample__delta': 3, 'beta': 2}
# gamma is not shown in __dict__ because it is a class variable  
