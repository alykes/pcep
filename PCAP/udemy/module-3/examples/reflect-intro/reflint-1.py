def empty_strings(user_object):                         # we get the object as a parameter
    for prop_name in user_object.__dict__.keys():       # the __dict__ gets all the properties of an object in dict form, so we can use .keys() method
        prop_value = getattr(user_object, prop_name)    # checks all properties of the object one by one, returns the name of the given property
        if isinstance(prop_value, str):                 # checks if the variable is of the given type, here we are checking for str
            setattr(user_object, prop_name, '')         # takes the object, the name of the property and the new value to set it to, here it is an empty string ''

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

doc_alex = Doctor('Alexander', 'Smith')
doc_alex.introduce()
empty_strings(doc_alex)     # Will find the str properties and set them to empty
doc_alex.introduce()