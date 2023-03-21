### Print Command  
- stuff blah blah  

### Literals  
4 types of literals  
- Integers  
  Can be represented with _ as well 1_000_000 is 1 million  
  minus numbers as well  
  - Octals 0o 0O  
  - Hexadecimal 0x  
- Floating point numbers  
  Anything with a decimal part, even if it's x.0 or x. where x is an integer  
  Can be represented with e notation 1e-5 or 1E-5 (0.00005)  
- strings  
  represents text, wrapped in double or single quotes '""' "''" or escape them \' \" inside  
- Boolean  
  True (1) or False (0)  


### Arthimetic Operators  

Python has 7 types of operators  

|Add|Subtract|Multiply|Divide|Floor Divide|Modulo|Exponential|
|---|---|---|---|---|---|---|
| + | - | * | / | // | % | ** |

- **  
`print(2 ** 3)` returns an integer   
`print(2 ** 3.)` returns a float   

- \*  
`print(2 * 3)` returns an integer  
`print(2 * 3.)` returns a float  

- /   
`print(10 / 2)` NOTE: division always returns a float  

- //  
`print(10 / 2)` returns an integer  
`print(10 / 2.)` returns a float  
rounds the values to the lesser integer value  
example:  
`print(6. / 4)` `1.5`  
`print(6. // 4)` `1.0`  
example:  
`print(6. / -4)` `-1.5`  
`print(6. // 4)` `-2.0` NOTE: Rounds to the lesser integer value!  

- %  
`print(4 % 2)` `0`  
`print(5 % 2)` `1`  


  Binary Operators expect a value on the left and one on the right  
  Unary Operators only need a value on the right, eg `-2` `+2`  

- Priority  
```
+ -
**
* / // %
+ -
```
`print(10-6**2/9*10+1)`  
`6 ** 2` `36/9` `4*10` `10-30+1`  
`-29`  
Sub-expressions are calculated first  
`print(2 * (5 - 2))`  
`10`  

### Variables
If you want to use a reserved keyword for a variable name, you can change the case of the variable name  
`finally` X  
`Finally` ✓  

### Inputs
always a string  
a program that doesn't use any inputs is called a **deaf** program

### String methods
```
print('ha' * 3)
"hahaha"
print("ha" * 0)
""
print("ha" * -1)
""
```  
`print(int("22"))`  

### Comparison Operators
|Equals|Not Equals|Greater Than|Greather Than or Equals|Less Than|Less Than or Equals|
|---|---|---|---|---|---|
| == | != | > | >= | < | <= |

### while blocks

```
while condition_is_true:
    do_stuff()
else:
    print("Getting out of the loop")
```  
`else` blocks are always run at the end of a loop  


### for loops
for i in ...:  

`range(5):` 0 1 2 3 4  
`range(1,5):` 1 2 3 4  

`break` exits the loop  
`contiue` skips the iteration  

### Bitwise operators

Summary:  
- Logical Operators `and` `not` and `or` return boolean values.  
- Bitwise Operators `&` `|` `^` and `~` allow you to manipulate single bits of data and return 0 or 1 based on the value of the bits that are used.  
- Bit shifting Operators `<<` `>>` allows you to shift bits to the left or right based on the amount of places specified.  


- & (AND operator)  
`print(15 & 22)` = `6`  
```
0b01111 +
0b10110
-------
0b00110
```

- | (OR operator)  
`print(15 | 22)` = `31`  
```
0b01111 +
0b10110
-------
0b11111
```

- ^ (exclusive OR)  
`print(15 ^ 22)` = `25`  
```
0b01111 +
0b10110
-------
0b11001
```


- ~ (negation)  
`print(~7)` = `-8`  
`print(~-7)` = `6`  

- Shortcut operators  

|Without Shortcut Operator|With Shortcut Operator|  
|---|---|  
|bit1 = bit1 & 22|bit1 &= 22|  
|bit1 = bit1 \| 22|bit1 \|= 22|  
|bit1 = bit1 ^ 22|bit1 ^= 22|  

#### Bit Shifting

- Shifting Right  
`print(22 >> 1)` = `11`  
0b10110 shift to the right by 1 bit  
0b01011 => 11  

`print(22 >> 2)` = `5`  
0b10110 shift to the right by 2 bits  
0b00101 => 5  

- Shifting Left  
`print(22 << 1)` = `44`  
0b10110 shift to the left by 1 bit  
0b101100 => 44  

`print(22 << 2)` = `88`  
0b10110 shift to the left by 2 bits  
0b101100 => 88  

- There is a pattern here  
print(22 >> 1) = print(22 // 2)  
print(22 >> 2) = print(22 // 4)  

print(22 << 1) = print(22 * 2)  
print(22 << 2) = print(22 * 4)  

### Lists
- Indexes start from 0  
- Can update a list item with `some_list[0] = 'whatever'`  
- Can delete a list item with `del some_list[0]`  
- Get the length of the list `len(some_list)`  
- Last element `some_list[-1]`  
- When creating lists, you create a pointer to reference the list; that's why the following result occurs  
  ```
  ages = [21, 43, 74, 24]
  ages2 = ages
  ages[0] = 92
  print(ages[0])
  print(ages2[0])
  ```
  ```
  result
  92  
  92
  ```

#### List methods
- `some_list.append()`  - Adds to the end of the list  
- `some_list.index(1)` - Will return the value in element 1 of the array
- `some_list.insert()`  - Inserts a value at the index specified `some_list.inset(2, 'Italy')`  
- `some_list.reverse()` - Sorts the list elements in a reversed order, this modifies the original array  
- `some_list.sort()` - Sorts the list elements, this modifies the original array  
- `some_list[0], some_list[1] = some_list[1], some_list[0]` - This will swap elements in a list  


#### Slicing a list
`list1[start:stop]`  # items start through stop-1  
`list1[start:]`      # items start through the rest of the array   
`list1[:stop]`       # items from the beginning through stop-1  
`list1[:]`           # a copy of the whole array  
`list1[start:stop:step]` # start through not past stop, by step  

`a[-1]`    # last item in the array  
`a[-2:]`   # last two items in the array  
`a[:-2]`   # everything except the last two items  

Similarly, step may be a negative number:  

`a[::-1]`    # all items in the array, reversed  
`a[1::-1]`   # the first two items, reversed  
`a[:-3:-1]`  # the last two items, reversed  
`a[-3::-1]`  # everything except the last two items, reversed  


Practical example:  
list1 = [10, 11, 12, 13, 14]  
print(list1[::1]) = [10, 11, 12, 13, 14]  
print(list1[::2]) = [10, 12, 14]  
print(list1[::3]) = [10, 13]  

print(list1[::-1]) = [14, 13, 12, 11, 10]  
print(list1[::-2]) = [14, 12, 10]  
print(list1[::-3]) = [14, 11]


Creating a new list from an existing list using slicing  
letters = ["G", "H", "O", "S", "T"]  
sub_letters = letters[1:] ==> `["G","H","O"]`  

Quirky list  
`list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]` is acceptable  
print(list1[5]) => 2.22  
print(list1[3][1]) => 55  

#### Searching elements
letters = ["G", "H", "O", "S", "T"]  
print("G" in letters) ==> `True`
print("Z" not in letters) ==> `True`

### List comprehension
matrix = [[j for j in range(4)] for i in range(4)]  
print(matrix[3][1])  
==> 1  

creates [[0, 1, 2, 3],[0, 1, 2, 3],[0, 1, 2, 3],[0, 1, 2, 3]]  

### Functions
- starts with `def name_of_function():`  
- Use `return` to return a certain value  
- return stops the remainder of the code in the function
- Position of the argument is important  
- Named parameters should be defined if you want to set values to specific parameters  
- Default values are set when defining the function  
- Functions return None if nothing is there is no `return` value  
- List as an argument

```
def multiply_values(lists):
  multiplied_values = []

  for item in list:
    multiplied_values.append(item * 2)

  return multiplied_values

multiply_values([1, 2, 3])
```
This will return a new list with the modified values  

#### Scope of variables  
- Anything decalred in a function will be available within that function  
- You can use the keyword global to access the variable in and old of that function  
- Lists act differently, they are referenced by memory location, regardless of where you change the list, it will **always** change!
- If the number of arguments is unknown, we can add a * before the parameter name ==> `def my_function(*students):`  
- A function variable can be accessed from a function within a function  
```
def my_function():
  x = 20
  def my_inner_function():
    print(x)   # This will print 20
  my_inner_function()
my_function()
```  

### Tuples
- One item tuple must be specified like `some_tuple = (1,)` or `some_tuple = 1,`  
- Defining a tuple `some_tuple = (1, 2, 3)` or `some_tuple = 1, 2, 3`  
- Tuples are immutable (the data cannot change)  
- `some_tuple.append("value")` does not work and gives an `AttributeError`  
- `some_tuple[0] = "value2"` also does not work and gives a `TypeError`  
- `del some_tuple[0]` does not work either and gives a `TypeError`  
- You can slice a tuple  

### Dictionary  
- Defining a dictionary  
```
usernames = {
  "ango": "ango_user",
  "Joe" "ninja",
  "Sarah": "bubble"
}
```
- Printing to dictionary  
  `print(usernames)`  
- To access data in a dictionary:  
  `print(usernames["ango"])` ==> `'ango_user'`  
- If the key doesn't exist, you get a `KeyError`
- If you have the same value for a key, the last one defined is printed!
```
testdict = {
  "brand": "apple",
  "ram": "3",
  "year": 2020,
  "year": 2021
}
```  
`print(testdict)`  
`{'brand': 'apple', 'ram': '3', 'year': 2021}`  


#### Dictionary Methods
- .keys()  
  This will return a list of keys  
  `dict_keys(['ango', 'Joe', 'Sarah'])`  
  This is the best approach to iterate over the keys (because you can't iterate a dictionary with a regular `for` loop like you can with `lists` and `tuples`)  
  ```
  for key in usernames.keys():
    print(key + " - " + usernames[key])
  ```  
  The result:   
  ```
  ango - ango_user
  Joe - ninja
  Sarah - bubbles
  ```
- .values()  
  This will return a list of values  
  `dict_values(['ango_user', 'ninja', 'bubbles'])`  
  This is the best approach to iterate over the values
- .items()  
  This will return the items as a tuple as a key/value pair  
  `dict_items([('ango', 'ango_user'), ('Joe', 'ninja'), ('Sarah', 'bubbles')])`  
- Modifying a single dictionary value  
  to update a value, you can need to reference the key as follows: `usernames["ango"] = "ango_admin"`  
- Adding a new key value pair  
  Two methods can be used:  
    - `usernames["tango"] = "tango_user"` to append a new value to the end of the dictionary  
    - `usernames.update({"tango": "tango_user"})` this also appends to the end of the dictionary  
- To delete a kay/value pair, you need to reference the key as follows: `del usernames["Joe"]`  
- To remove all items, you can use the `.clear()` method as follows: `usernames.clear()`  
- To remove the last item, you can use `.popitem()`  
- To copy a dictionary, you can use the `.copy()` method  
  `usernames_backup = usernames.copy()`  

### Error Handling  
- TypeError - Wrong data types passed in operations and functions  
- ValueError - Wrong values passed in operations and functions  
- NameError - When a variable isn't defined  
- Multiple exceptions should be defined in brackets and with a , between them  
  `except (TypeError, ZeroDivisionError)`  
- Using the `raise` keyword  
  Inside the try block together with a named exception  
  Inside the except block, but unnamed  