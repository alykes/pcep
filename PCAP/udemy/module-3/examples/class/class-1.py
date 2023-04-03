class User:
    def __init__(self):
        self.nickname = 'DJ Ango'
        self.city = 'Ελλαδα'
    
    def introduce(self):
        print('Hello, I\'m', self.nickname, 'and I\'m smashing it out in', self.city)

munga = User()          # Creates the object
munga.introduce()       # Runs the method on the object

print(munga.nickname)   # Access to variables in the class
print(munga.city)       # Access to variables in the class

