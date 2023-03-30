import sys

def exit():
    print("Let me exit malaka!")

for name in dir(sys):
    print(name)

exit() # This will just print the statement "Let me exit malaka!" and not exit, you also need to specify the module name

# Using a method is as simple as writing the module name and then calling the method
sys.exit()

# Attempting to use a function that doesn't exist will print an Attribute Error
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'sys' has no attribute 'exit_mumbo_jumbo'
'''

