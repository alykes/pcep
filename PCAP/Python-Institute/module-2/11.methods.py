# Demonstrating the capitalize() method:
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())    # all characters are converted to lowercase, the first element is not a letter.
print('123'.capitalize())       # nothing happens, first element is not a letter.
print("αβγδ".capitalize())      # converted to an uppercase letter of that language
print("a noble bonker. what a hero".capitalize())


# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center(20, '*') + ']')


# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

# the second argument is the starting position to search from
print('kappa'.find('a', 2))

# Searching a block of text for each occurence of the string
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

# the second argument is where to start from and the third argument is where to end the seach (not inclusive)
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))


# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())


# Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())


# Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())


# Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

# Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demonstrating the join() method:
# If the list doesn't contain all strings, then there will be a TypeError returned.  
print(",".join(["omicron", "pi", "rho"]))

# Demonstrating the lower() method:
print("SiGmA=60".lower())

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")

print("www.cisco.com".lstrip("w."))         # returns cisco.com
print("www.cisco.com".lstrip(".w"))         # Any order works so long as the letters all exist at the beginning of the string
print("vvv.www.cisco.com".lstrip("w."))     # returns the original string because the letters don't all exist at the start of the string

print("vvv.www.cisco.com".lstrip("w.v"))    # returns cisco.com
print("www.cisco.com".lstrip("w.c"))        # returns isco.com

print("pythoninstitute.org".lstrip(".org")) # returns pythoninstitute.org , because .org (or a combination of those letters doesn't exist at the beggining of the string)


# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# The third argument limits how many replacements should occur
print("This is it!".replace("is", "are", 1))
print("This is it, is it? Yes, it is!".replace("is", "are", 3))


# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))        

print("tau tau tau".rfind("ta", 9))     # Pay attention to these two examples
print("tau tau tau".rfind("ta", 8))

# Search a string between the first index (inclusive) and the second index (exclusive)
print("tau tau tau".rfind("ta", 3, 9))  
print("tau tau tau".rfind("ta", 3, 10)) 

# Demonstrating the split() method:
print("phi       chi\npsi".split())     # splits by whitespaces

# You can also specify where to split the string
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)


# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))
print()

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")


# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))
print()

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")
print("[" + " moo, sun, fun, run ".strip(", mo") + "]")     # removes the supplied characters from the beginnind and end only, regardless of order!
print("[" + " moo, sun, fun, run , ".strip("o, m") + "]")

# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())
print()

# Demonstrating the title() method:
print("I know that I know noThing. Part 1.".title())
print()

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())
