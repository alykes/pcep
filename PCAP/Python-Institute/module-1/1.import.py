# This shows that pi is two distinct entities in the various namespaces
# and the entities do not affect one another.
import math

def sin(x):
    if 2 * x == pi:
        return 0.999999999999999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))
