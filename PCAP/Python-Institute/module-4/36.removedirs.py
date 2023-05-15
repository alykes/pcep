# Create and delete dirctories
import os

os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())

# Remove Multiple directories
os.makedirs("my_third_directory/my_fourth_directory")
print(os.listdir())
print(os.listdir('my_third_directory'))
os.removedirs("my_third_directory/my_fourth_directory")
print(os.listdir())


