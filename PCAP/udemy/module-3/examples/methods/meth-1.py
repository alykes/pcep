class Doctor():
    def __init__(self, first_name = 'John', last_name = 'Smith'):
        self.first_name = first_name
        self.last_name = last_name
        self.__format_names()       # This is a call to a private method

    def __format_names(self):
        self.first_name = self.first_name.title()   # Make the first letter of each word upper case and the rest lower case
        self.last_name = self.last_name.title()

    def introduce(self):
        print('Hi, I am', self.first_name)

    def compare_name(self, name_to_compare):
        if self.first_name == name_to_compare:
            print('We have the same name!')
        else:
            print('Oh, we have different names!')
    
    def get_first_last_name_together(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):              # This will override the default output of the object, print(doc_alex)
        return 'Doctor:' + self.first_name + ' ' + self.last_name
    
doc_alex = Doctor('AleXandeR', 'SMith')
doc_alex.introduce()
doc_alex.compare_name('John')
print(doc_alex.get_first_last_name_together())

print(doc_alex.__dict__)
print(Doctor.__dict__)