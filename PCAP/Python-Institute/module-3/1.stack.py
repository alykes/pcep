# Implementation of a stack using a procedural approach

stack = []

def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(1)
push(2)
push(3)

print(pop())    # 3
print(pop())    # 2
print(pop())    # 1

