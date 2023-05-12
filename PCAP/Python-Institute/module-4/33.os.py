import os
print(os.uname())       # Only works on some unix systems.

print(os.name)          # Will return one of posix, nt or java(if your code is written in Jython) 


import platform         # This can be used for windows to get a similar result
print(platform.uname()) # Used in windows to get a similar result.
