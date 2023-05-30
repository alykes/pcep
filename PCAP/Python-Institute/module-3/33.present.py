class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy


sun = Star("Sun", "Milky Way")
print(sun)
print(Star)

# Result 
# <__main__.Star object at 0x7f1074cc7c50>
# <class '__main__.Star'>