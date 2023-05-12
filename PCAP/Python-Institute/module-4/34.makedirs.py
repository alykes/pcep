# An example of makedirs() and chdir()
# note makedirs() creates directories recursively
import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())     # contents are returned as a list.