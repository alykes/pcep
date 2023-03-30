import platform

print(platform.platform())                  # Linux-5.10.102.1-microsoft-standard-WSL2-x86_64-with-glibc2.35
# aliased will return any other underlying values, it might do anything on certain platforms
print(platform.platform(aliased = True))    # Linux-5.10.102.1-microsoft-standard-WSL2-x86_64-with-glibc2.35
# if terse is true, it will try to return a shorter version of the output on certain platforms
print(platform.platform(terse = True))      # Linux-5.10.102.1-microsoft-standard-WSL2-x86_64-with-glibc2.35
# Setting both to true will show a shorter and aliased version of the output on certain platforms
print(platform.platform(True, True))        # Linux-5.10.102.1-microsoft-standard-WSL2-x86_64-with-glibc2.35



print(platform.machine())       # x86_64 ==> returns the short name of the processor
print(platform.processor())     # x86_64 ==> returns the real name of the processor (might print the same info as machine())
print(platform.system())        # Linux ==> This will return the Generic Operating System name: Windows, Linux etc
print(platform.python_implementation()) # CPython ==> You should normally expect to see CPython
print(platform.python_version_tuple())  # ('3', '10', '6') ==> This will return the python version as a tuple
