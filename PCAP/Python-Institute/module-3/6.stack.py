## Same as 5.stack.py but uses two stacks.
# Showing that they work independently

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object_1 = Stack()
stack_object_2 = Stack()

stack_object_1.push(3)
stack_object_2.push(stack_object_1.pop())   # The number popped from the 1st stack object is pushed onto the 2nd stack object

print(stack_object_2.pop())
