class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    def get_counter(self):
        return self.__counter

    def pop(self):
        self.__counter += 1
        val = Stack.pop(self)

        return val
	
    def push(self, val):
        #self.__counter += 1
        Stack.push(self, val)

stk = CountingStack()
for i in range(100):

    if i % 10 == 0:
        print("i:", i, "counter:", stk.get_counter())
        
    stk.push(i)
    stk.pop()

        
print(stk.get_counter())

