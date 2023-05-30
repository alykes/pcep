def read_int(prompt, min, max):
    #
    while True:
        try:
            num = int(input(prompt))
            if num < min or num > max:
                print("Error: the value is not within permitted range (min..max)")
                continue
            return num
            
        except ValueError:
            print("Error: wrong input") 
    #

v = read_int("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
