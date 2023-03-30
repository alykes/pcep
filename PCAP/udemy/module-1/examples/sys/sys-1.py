"""
Retuns a list of locations that Python checks for modules
When Python finds the module, even though it might reside in mulitple locations, it will not keep searching. Takes the first one it finds.
"""
import sys

# print(sys.path)

for path in (sys.path):
    print(path)