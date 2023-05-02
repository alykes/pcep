# Calculates your digit of life by summing the numbers in your birthday until a single digit remains.
try:
    dob = int(input("Please enter your date of birth (DDMMYYY): "))
except:
    print("The input needs to be numbers only.")
    exit()

while len(dob) > 1:
    sum = 0 

    for char in dob:
        sum += int(char)

    dob = str(sum)

print("Your Digit of Life is: ", sum)