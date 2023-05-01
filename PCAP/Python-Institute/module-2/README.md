## Python Essentials 2  

<ins>Strings, String and List Methods, Exceptions</ins>  

In this module:  
- Characters, strings and coding standards;  
- Strings vs. lists – similarities and differences;  
- Lists methods;  
- String methods;  
- Python's way of handling runtime errors;  
- Controlling the flow of errors using try and except;  
- Hierarchy of exceptions.  

### Module 2.1  
#### Characters and Strings  

Characters are stored as numbers  
There are standard characters, whitespace and control characters (as they control input/output devices)  
The standard is ASCII short for **American Standard Code for Information Interchange**. 
  There is space for 256 characters in total  
  The first 128 chars are the most important  

ASCII uses **8 bits** for each **sign**  

The word internationisation is often abbreviated to `IN18N`  

- **Code Points and Code Pages**  
  - A code point is a number that makes a character, e.g., `32` is a code point for `space`  
  - standard ASCII has `128` code points  
  - the remaining code points can be used for other character sets  
  - A `code page` is a standard for using the upper 128 code points to store language specific characters  
    There are different code pages for Greek, Western European, Eastern European etc  

- **Unicode**  
  - Code Pages helped solve some internationalisation (I18N) issues  
  - Unicode solves the problem in the longterm  
  - Unicode assigns unique (unambiguous) characters to more than a million code points  
  - The first are identical to ASCII, the first 256 are identical to the ISO/IEC 8859-1 code page (Western European Languages)  
  - Two different methods of using and storing characters are `USC-4` and `UTF-8`  

- **UCS-4**  
  - Unicode doesn't say anything about how to code and store the characters in memory or files, it just names and assigns them to _planes_ (groups of characters with similar origins)  
  - `Universal Character Set` is the expanded name of _USC_  
  - **USC-4** uses 32 bits for each character, the code is just a `Unicode Code Point`.  
  - A file containing USC-4 encoded text may start with a BOM or `byte mark order` which announces the nature of the file contents (e.g., UTF-8 or USC-4).  
  - USC-4 (32 bits) is 4 times larger than ASCII (8 bits) for each character.   

- **UTF-8**  
  - `Unicode Transformation Format` is the expanded form for _UTF_  
  - UTF only uses as many bits that _it requires_ to represent a **code point**  
    - all Latin characters use eight bits (standard ASCII)  
    - non-Latin occupy 16 bits  
    - CJK (China Japan Korea) use 24 bits  
  - Python 3 fully support Unicode and UTF-8  

_Python 3 is fully compatible I18N_  

<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-92  


### Module 2.2  
#### Strings  

_Revision_  
- Strings are immutable sequences  
- `len()` of strings also counts whitespaces like `\n` and spaces, refer to `1.strings.py`  
- multiline strings, denoted by `'''` or `"""`, refer to `2.strings.py`  
- concatenating and replicating strings. The operator `+` is commutative, unlike the numerical version, refer to `3.strings.py`  
- `ord()` ordinal of a string, is the numerical representation or the code-point value. Refer `4.strings.py`  
- `char()` get the character from an interger value, refer to `4.strings.py`  
- indexing, strings are sequences, you can treat them like lists (even though they aren't exactly lists). Refer `5.strings.py`  
- slices, you can slice up a string, just like a list. Refer `6.strings.py`  
- `in` and `not in` operators, refer `7.strings.py`  
- Strings are immutable, so you can't run the following as you will get an error for each:
  - `del some_string[0]` = **ERROR**, although, you can still run can still run `del some_string`successfully  
  - `some_string.insert(0, "A")` = **ERROR**  
  - `some_string.append("Z")` = **ERROR**  
- To concatenate to a string, simply use the `+` operator:  
  - `some_string = 'a' + some_string`  
  - `some_string = some_string + 'a'` 
- `min()` the min function can be used on a string, it basically compares the ASCII values (code point values), refer `8.strings.py`  
- `max()` the max function can be used on a string, it basically compares the ASCII values (code point values), refer `8.strings.py`  
- `.index()` **method** (not a function) searches the sequence from the beginning, in order to find the first element of the value specified in its argument. Refer to `9.strings.py`  
  - returns a **ValueError** if the string is not found!  
- `list()` converts a string to a list, containing a single character per element. Refer `10.strings.py`  
- `count()` counts the occurence of the the argument in the string.

<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-93  


### Module 2.3  
#### String Methods  

Refer to `11.methods.py` and `lab2.3.1.18.py`  
- `.capitalize()` - creates a new string and captialises only the first character if it is a letter, all remaining strings will be converted to lowercase.  
- `.center(x)` - where x is a filed value, basically aligns the string in a field that has width x. A second argument can be passed and used instead of a space.  
- `.endswith()` - checks if the given string ends with the specified argument and returns `True` or `False`.  
- `.find()` - similar to index, searches for a substring and returns the index of the first occurrenxce of this substring but:  
  - safer as returns `-1` if it doesn't find the string and not an error.  
  - works with **strings** only.  
- `.isalnum()` - checks if the string contains **only digits or alphabetical characters (letters)**, and returns `True` or `False` according to the result.  
- `.isalpha()` - checks if the string contains letters only.  
- `.isdigit()` - checks if the string contains digits only.  
- `.islower()` - checks if the string contains lowercase letters only.  
- `.isspace()` - checks if the string contains whitespaces only, this includes `\n`, `\t` and obivously ` `.  
- `.isupper()` - checks if the string contains uppercase letters only.  
- `.join()` - will join strings together from a **list** of _strings only_ with a specified seperator, e.g., `print(",".join(["omicron", "pi", "rho"]))` will print `omicron,pi,rho`.  
- `.lower()` - converts any letters found in a string to all lowercase letters.  
- `.lstrip()` - removes all **leading whitespaces** as a default, you can also specify any other letters to remove from the **l**eft side of the string.  
- `.replace()` - replaces the first string with the second string. A third argument limits how many replaces should occur.  
- `.rfind()` - starts from the end of a string and works backwards. **NOTE: If one argument is supplied, it starts the search from the index to the end of the string.**   
- `.rstrip()` - same string strip() but affects the **r**ight side of the string!  
- `.split()` - splits a string by whitespaces and returns a list of strings. Accepts arguments to perform the split on as well.  
- `.startswith()` - same as `endswith()` but checks from the start.  
- `.strip()` - strips all leading and trailing whitespaces. If a second argument is supplied, it will remove those characters from the **start and end** of the string only, regardless of their order.  
- `.swapcase()` - changes the case of all letters found in the string, lower to upper and vice versa. All other characters remain untouched.  
- `.title()` - capitalises each letter of a word and changed the rest of the letters to lowercase.  
- `.upper()` - changes all letters to uppercase.  

<ins>Refer to the summary page here</ins>  
https://edube.org/learn/pe-2/section-summary-94  



### Module 2.4  
#### Strings in Action and List Methods   

- Comparing  

Python's strings can be compared using the same set of operators which are in use in relation to numbers.

Take a look at these operators - they can all compare strings, too:
- `==`  
- `!=`  
- `>`  
- `>=`  
- `<`  
- `<=`  

Python just compares code point values.  
Upper case letters have smaller integer values than lower case letters.  
If a string contains only digits it's still a string!  

**NOTE:** When comparing a string to an integer value, you can use `==` (will always return `False`) and `!=` (will always return `True`), other operators will give you a TypeError.  


- Sorting  
  Sort a list containing strings can be achieved by various ways  
  - `sorted()` function doesn't change the list and only returns a new list.  
  - `.sort()` method will sort the list in-place

- Converting numerical values to strings and vice versa.  
  - Can be achieved as long as the strings and numerical values are in the right format to be converted.  
  - Refer to `14.conversions.py`  

<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-95  


### Module 2.5  
#### Four Simple Programs  

This module contains 4 simple programs, as the title states and basica explanations for them.


