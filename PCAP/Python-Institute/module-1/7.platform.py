import platform

#for name in dir(platform):
#    print(name, end='\n')

print(platform.platform(aliased = False, terse = False)) # these are the two arguments, they are false by default

print(platform.platform())          # set to false for both aliases and terse
print(platform.platform(1))         # aliased
print(platform.platform(0, 1))      # aliased, terse

print(platform.version())           # returns the OS version

print(platform.python_version())    # returns Python version as a string
print(platform.python_version_tuple())  # returns Python version as a tuple
print(platform.python_implementation)   # returns the type of Python, generally this is CPython

print(platform.machine())   # returns the generic name of the processor
print(platform.processor()) # returns the actual/real name of the processor

print(platform.system())    # returns the generic name of the OS
print(platform.version())   # returns the OS version
