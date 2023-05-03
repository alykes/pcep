class Stack:
    def __init__(self):
        self.__stack_list = []          # Creates an empty list and makes it private

stack_object = Stack()                  # Creates the object from the class Stack and assigns it to a variable

print(len(stack_object.__stack_list))   # Now, to reference the object property you need to add the __

