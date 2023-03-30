## Strings  
This module will cover strings  

### Internal String Representation
- Text value, with single or double quotes  
- Stores as numbers in memory, this is known as `charater encoding`  
- Commonly used encoding, ASCII (American Standard Code for Information Interchange) 256 characters (1 byte or 8 bits), first 128 are the most significant.  
  - 'a' is 97, 'A' is 65, + is 43, space is 32. There integer numbers are called `code points`.  
  - The second half of the ASCII code page can be used with other code pages such as Greek code page, Cyrillic code page, Eastern Europe code page.  
  - The first half of the ASCII code page remains the same in all other code pages, so Greek will use the standard ASCII code points in the first half 0-127, then it's own from 128-255.  
  - The second half 128-255 is called the extended ASCII characters.  
  - The concept to finding a solution for multiple languages is called `internationalisation` and is abbreviated as `i18n` (18 is for 18 characters).  
  - Unicode does not use code pages, each char has it's only unique number (code point).  
    - over 1 million code points can be stored.   
    - First 128 code points of ASCII  
    - The second 128 code points are identical to the code page designed for Western Languages  
    - Each character can be placed in a plane, there are 17  
        - The first one is the `Basic Multilingual Plane` (Basic Multilingual)  
        - The second is the `Supplementary Ideographic Plane` (Japanese or Korean)  
    - Unicode can be implemented using  
      - `UTF-32`
      - `UTF-8` - compatible with ASCII, uses as many bits as needed (from 8 to 32 bits). ASCII chars are 8 bits, Non-Latin are 24 bits, Chinese/Japanese/Korean are 32 bits. Fully supported in Python!  
      - `UCS-4` - Universal Character Set - 32 bits per character (4 bytes), takes up a lot of space! 4x more than ASCII.  

### String basic operations
- They are immutable sequences  
- `len()` - how many chars in a string  
- `[]` - indexing to get char at an index  
- `[:]` - slicing can also be used  
- Some characters need to be escaped such as ' eg `print('Yiasou, you\'re a vlaka')`  
- `ord()` - returns the code point or integer of a single character, eg `ord('a')` => 97  
- `char()` - returns the character from an integer value representing the code point, eg `chr(97)` => 'a'  
- `min()` - will find the character with the lowest ASCII code point, eg, `min(angoisthebest)` ==> 'a'  
- `max()` - will find the character with the highest ASCII code point, eg, `max(angorodeazebra)` ==> 'z'  
- multi-line strings should be encased in `'''` or `"""` - len() includes the new line character  
- Operator Overloading occurs when dealing with strings  
  - `+` concatenates the string  
  - `*` multiplies the string  
  - if the order `doesn't matter` between the operands, the operator is `commutative`  
  - if the order `does matter` between the operands, the operator is `non-commutative`  
- you can loop over strings with a for loop, eg `for char in 'hello vlaka': print(char, end='-')`  
- You CANNOT use the following on strings because they are immutable:  
  - del  
  - .insert()    
  - .append()  

### String Searches  
- `.index()` - returns the index of the first occurrence of the character.eg `'angoisthebest'.index('a')` => 0   
  - Python raises an error if the given value is not found in the string. `ValueError`  
  - index() can be used on other sequences, not just strings.  
- `.find()` - can only be used on strings.  
  - safer to use and doesn't return an error like `index()`, if a character can't found the character it will return -1.   
  - find() has a 2 and 3 argument variation:  
    - 2 arguments: searches from start_index (inclusive) to the end of the string `find('string', start_index)`  
    - 3 arguments: searches from start_index (inclusive) to end_index (exclusive) of the string `find('string', start_index, end_index)`  
- `.rfind()` - same as find() but searches for the first occurence from the end of the string to the start.  
  - rfind() has a 2 and 3 argument variation:  
    - 2 arguments: searches from start_index (inclusive) to the end of the string `rfind('string', start_index)`  
    - 3 arguments: searches from start_index (inclusive) to end_index (exclusive) of the string `rfind('string', start_index, end_index)`  
- `.isalnum()` - returns True is the string only contains alphanumeric characters  
- `.isalpha()` - returns True if the string only contains letters  
- `.isdigit()` - returns True if all the charactets in a string are all digits  
- `.islower()` - returns True if all the letters in a string are all lowercase. Can contain letters and other characters and still return True.  
- `.isupper()` - returns True if all the letters in a string are all uppercase. Can contain letters and other characters and still return True.  
- `.isspace()` - returns True if all characters are whitespace characters, also accepts a newline character (\n)  

### Joining, Splitting and Sorting Strings  
- refer to strings-2.py for some examples.  
- `.join()`  - Join strings together, take note of the syntax.  
- `.split()` - This will split the string, will remove excess whitespaces and use `\t`, `\n` and ` ` as delimters.  
- `.sort()` - This will sort the original list.  
- `sorted()` - The original list remains unchanged.  
- Use `sorted()` to _create a copy_, use `.sort()` to _sort the original list_  

### Comparing Strings  
- refer to strings-3.py for some examples.  
- You can use the same operators that you use for number comparisons, eg `==` `!=` `>` `>=` `<` `<=`  
- Python checks the code points when performing < and > comparisons. **Note** that uppercase characters are lower in number!  
- Python searches for the first differing character only and checks them against one another!  
