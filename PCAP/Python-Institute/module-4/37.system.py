# Runs a command on the OS, if a zero is returned, then it means success!
import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)
