# ZeroDivisionError
value = 1
value /= 0      # This line will raise an exception called a ZeroDivisionError

# IndexError
my_list = []
x = my_list[0]  # This line will raise an exception called an IndexError


# A seemingly ok an example to check your input for validation but it actually bloats your code and can make it illegible.
# The best way is to rewrite this code with a try..except block!
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if second_number != 0:
    print(first_number / second_number)
else:
    print("This operation cannot be done.")

print("THE END.")


# This is the better way rewrite the code sample directly above.
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")


# This code jumps out of the try block before print("2") is executed
try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")


# The following try..except block is a little ambiguous on what caused the actual exception
try:
    x = int(input("Enter a number: "))      # if you enter a letter, then this places the code in the except block
    y = 1 / x                               # if x is 0, then this places the code in the except block
except:
    # Both issues described above can land in the except block but you don't have a clear understanding of why it happened
    print("Oh dear, something went wrong...")

print("THE END.")

# The best approach to solve the issue above is to create a better try..except block
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")
