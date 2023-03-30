# Find all the entities that are available to us in the math module

import math

for name in dir(math):
    print(name, end='\t')