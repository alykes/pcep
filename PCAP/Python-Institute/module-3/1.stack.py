# A simple progrm showing how a stack works - LIFO
stack = []

def push(val):
    stack.append(val)
    print("pushing", val, "onto the stack:", stack)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)     # pushing 3 onto the stack: [3]
push(2)     # pushing 2 onto the stack: [3, 2]
push(1)     # pushing 1 onto the stack: [3, 2, 1]

print()

print(pop(),"removed from the stack:", stack)   # 1 removed from the stack: [3, 2]
print(pop(),"removed from the stack:", stack)   # 2 removed from the stack: [3]
print(pop(),"removed from the stack:", stack)   # 3 removed from the stack: []

