print("I like to be a module.")
print("The value of __name__ is:", __name__)

if __name__ == "__main__":
    print("!!!Naughty!!! Running the module directly!")
else:
    print("Yay! Running this as a module!")