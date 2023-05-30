# Determine whether text input is a palindrone or not
# A palindrome is a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.
text = input("Please enter a word: ")

string = ""
# Get rid of all the whitespaces
for char in text:
    if char.isspace():
        continue
    else:
        string += char.upper()

last_index = rindex = len(string) -1

index = 0
palindrone = True

while palindrone and index <= last_index:
    if string[index] == string[rindex]:
        index += 1
        rindex -= 1
    else:
        palindrone = False
        break

if palindrone:
    print("It is a palidrone!")
else:
    print("It is not a palidrone.")
