# Looks for the letters from the first string, to see if they are in the second string
# Doesn't take into consideration unique letters (repeated letters)
string_one = input("Please enter a string to search for: ")  # dog
string_two = input("Please enter a string to search through: ") # randomcrapgoingoninhere

# Prep the variables
string_one = string_one.lower()
string_two = string_two.lower()
found = -1
current_pos = 0

# Search for the characters from the first string in the second, the order must match.
for char in string_one:

    found = string_two.find(char)

    if current_pos > found or found == -1:
        # Set found to -1 if current_pos is > found, it means the letters aren't in the right order
        found = -1
        break

    current_pos = found


if found != -1:
    print("All the letters are in the second string")
else:
    print("Not all letters were found or are in the correct order!")