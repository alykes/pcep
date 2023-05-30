# Adding some more examples on how to use a superclass variables(properties) and override some methods
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)                        # you can also use this instead -->     super().__init__()
        self.__sum = 0
    
    def total_sum(self):
        # return self.__sum                         # This simplifies the code into one line as you don't need to iterate over elements
        total = 0
        for elem in self._Stack__stack_list:        # this is how you access the stack_list as it's part of the Stack Superclass
            total += elem
        return total
    
    def push(self, val):                            # This adds the new value to the __sum value
        self.__sum += val
        Stack.push(self, val)

    def pop(self):                                  # This subtracts the new value from the __sum value
        # self.__sum -= self._Stack__stack_list[-1] # You can use this method also``
        # return Stack.pop(self)                    # They both work different ways but with the same result
        val = Stack.pop(self)
        self.__sum -= val
        return val

        



st = AddingStack()

st.push(1)
st.push(2)
st.push(3)
st.push(4)

print(st)
print(st._Stack__stack_list)
print(st.total_sum())
print(st._AddingStack__sum)

print("Popping:", st.pop())
print(st._Stack__stack_list)
print(st._AddingStack__sum)

# Result:
# <__main__.AddingStack object at 0x7fac06521650>
# [1, 2, 3, 4]
# 10
# 10
# [1, 2, 3]
# 6