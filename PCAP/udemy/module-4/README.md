## Exceptions  
Will gloss over this topic as it's the same content as PCEP.  
From the course notes...  
```
However, in case of exceptions, it seems that both exams require the knowledge of exceptions basics. 
I also got a written confirmation from the Python Institute that this is the case: even though PCEP 
now verifies your exception basics knowledge, the same kinds of questions can reappear in the more 
advanced PCAP exam.
```  

### What is an exception?  
Exception is an exvent which occurs during the execution of a program that disrupts the normal flow of the program instructions.   
Python `raises` an exception.  

### Types of Errors  
- Indentation Error  
  - This is a form of a syntax error  

- Value Error  
  - Syntactically correct but can't perform the function  
  ```
  value = int(input('Please enter an integer:'))
  ```  
  If the user types `a`, a ValueError is raised. `ValueError: invalid literal for int() with base 10: 'a'`  

- Type Error  
  - Type of data you are trying to use is not correct for a given function  
  ```
  value = 'aidi'
  print('Let's see here, this is the new string:', value + 10 )
  ```  
  `TypeError: can only concatenate str (not "int") to str`  

- Zero Division Error  
  `print(1/0)` this will raise a zero division error.  


### Try Except Blocks
- Named exceptions should be placed at the top with a catch-all exception type at the bottom of the list.  
- Syntax errors can't be caught unless they are raised manually. `raise SytaxError`  
- Only one excpetion block is used  

### Exception Hierarchy  
- Everything pretty much goes back to the `BaseException` type.  

### Assertions  
- They are not an input validation tool.  
- They can be turned off when you publish your code.  

### Else branch with Try..Except  
- Will only run the `else` branch `if no exception is raised` in the try..except block.  

### finally keyword  
- `finally` is ALWAYS executed, whether or not an exception is raised!  
- `finally` appears after the else block, they are not dependant on each other.  

### raise keyword  
- This is used by a developer to raise an exception on your own.
  - When writing tests.
  - Another part of the program to be respnsible for the exceptions.  
- You can use the raise keyword if you want to handle an exception partially.  

### Exceptions as Objects  
- Exceptions in Python are objects.  
- You need to extend your exception block using `as` if you would like to get detailed information about exactly what went wrong! Refer `exc-4.py`  
- As soon as you use `as`, you can refer to the exception within the except block with the identifier (for example `e`)  
  - when you print the object, the exception class actually implements a version of the `__str__` method that will give you detailed information and a meaningful message.  
- Each exception class that inherits from `BaseException` has a property named `args`, it's a tuple that contains all the arguments passed to the constructor.  
- All the details passed to the constructor are added to the args property, this feature is used to pass details about why the exception is raised.  

### Creating your own exceptions  
- There classes like any other, you can add inheritances to create your own exception types by adding the Super Class to inherit in your own exception.  
- Use a similar exception class as the Super Class, to the exception that you would like to create.  
- Refer to `exc-7.py` for an example.  
