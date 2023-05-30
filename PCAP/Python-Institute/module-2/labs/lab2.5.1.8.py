# Finding anagrams from two strings
# An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. 
# For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.
def remove_spaces(text):
    temp_string = ''
    
    for char in text:
        if not char.isspace():
            temp_string += char.upper()
        else:
            continue
    return temp_string


def create_list(strng):
    temp_list = []

    for char in strng:
        temp_list.append(char)

    return temp_list



# Start of the main program
text_one = input("Please enter a word: ")
text_two = input("Please enter another word: ")
if len(text_one) != 0 and len(text_two) != 0:
    list_one = []
    list_two = []
    anagram = True

    # Remove spaces from the strings
    string_one = remove_spaces(text_one)
    string_two = remove_spaces(text_two)

    # Create the lists from the two strings
    list_one = create_list(string_one)
    list_two = create_list(string_two)

    # This is where the heavy lifting is done
    for element in list_one:
        if element not in list_two:
            print("Not an anagram")
            anagram = False
            break
        else:
            list_two.remove(element)

    if anagram and not list_two:
        print("*** ANAGRAM FOUND ***")
    else:
        print("This is not an anagram!")
else:
    print("Please ensure that there are no blank inputs!")