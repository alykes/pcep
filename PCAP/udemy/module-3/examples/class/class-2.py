class User:
    def __init__(self, nickname, city):
        self.nickname = nickname
        self.city = city
    
    def introduce(self):
        print('Hello, I\'m', self.nickname, 'and I\'m smashing it out in', self.city)

munga = User('ango', 'Αθηνα')          # Creates the object
munga.introduce()       # Runs the method on the object

allo = User('Skip', 'Perth')
allo.introduce()

print(munga.nickname)   # Access to variables in the class
print(munga.city)       # Access to variables in the class