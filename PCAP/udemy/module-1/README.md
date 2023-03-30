## Modules and Packages

### Summary of terms

- **Decomposition**: Is when you break down your code into smaller pieces that can be stored in separate files, so they are easier to maintain and develop.  
- **Modules**: A file that contains Python definitions and statements, these can be _imported_ into a second file.  
- **The Python Standard Library**: These are modules that are delivered with Python https://docs.python.org/3/library/index.html  
  - An example is the `sys` module, if you look through the doco, you will see the **entities** associated with it, eg. `sys.abiflags` `sys.audit` `sys.exit` etc...  
  - Entites describe all the variables and methods that can be used in your code if you import this module.  

### Importing Modules
- To make a module available in your code, simply use the following line of code.  
  `import sys`  
- All import statements should be placed at the very beginning of a code file.  
- You can also import modules on the same line as below  
  `import sys, math`  
- To find the entities that are available, you can use the `dir` keyword, refer to the `sys.py` example  
- Using a method is as simple as writing the module name and then calling the method  
  `sys.exit()`  
- If you try to use a method that doesn't exist, you will get an attribute error  
  `sys.exit_mumbo_jumbo()`  
- We can say that the `sys` module has it's own namespace, `exit()` is therefore within the `sys` namespace  
- If you import a function from a module and you have a deifinition in your code for the same named function, the one you have specifically written in your code will be used, refer to the `sys-3.py` example.  
- It's dangerous to use `from sys import *` as you import everything and you could have a bunch of function that you have created that may have the same function name. You may experience conflicts!  
- The difference between `import sys` and `from sys import *` is that you don't need to use sys with the latter (which means that you could potentially have conflicts with existing functions that have the same name)  
- Aliases: 
  - Module: You can use `import sys as s` so now you can use `s` as the namespace and `s.exit()` will be perfecting legal to use. Refer to the example `sys-4.py`  
  - Entities: You can give an entity as alias also `from sys import exit as bye_bye`, refer to the example `sys-5.py`  
  
### Math Module
- For PCAP, you need to know 6 of the functions that are available in the math module:
  - `ceil()` - returns whole number  
  - `floor()`  
  - `trunc()`
  - `factorial()`  
  - `sqrt()` - returns a float  
  - `hypot()` - returns a float  

### Random Module
- Python offers pseudo random numbers (there is generally a seed and then an algorithm runs over the top of it)  
- Python can give multiple numbers from the same seed  
- Ideally the seed should change over time, the easiest way is to use `time`  
- random produces a number from 0 to 1, refer to the example in `random-1.py`  
- For the PCAP exam, you will need to know the following functions:  
  - `random()` - randomly returns a value from 0 to 1
  - `seed()` - is used to set a static seed, which will then return the same "random" numbers everytime. Refer to the example in `random-2.py`  
  - `choice()` - takes in a sequence and returns a random element from the sequence, that could contain duplicates. Refer to the example in `random-3.py`  
  - `sample()` - sample will pick unique indexes from a sequence only once! Refer to the example in `random-4.py`
    NOTE: If the sequence contains identical elements, then they will not be considered 'unique' and will be returned as separte values, refer to the example `random-5.py`  
    If you specify a number greater than the amount of elements, you will get a `ValueError: Sample larger than population or is negative`  

### Platform Module
This will give you access to the underlying platform's identifying data. The module allows you to get information about the python version, the underlying OS platform and the hardware that is being used.  

|Layers|
|---|
|Your Code|
|Python|
|Operating System|
|Hardware|

- Functions that are required knowledge for the exam:  
  - `platform()` - the function takes 2 values that have defaults `platform.platform(aliased= False, terse= False)`  
    If `aliased` is set to anything other than `False`, it will try to return any other underlying names.  
    If `tersed` is set to anything other than `False`, it will try to return a shorter version of the output.  
  - `machine()` - this function will return the architecture of the current machine, generic name of the processor that runs the OS.  
  - `processor()` - similar function to the one above but returns the _real name_ of the processor.  
  - `system()` - This will return the Generic Operating System name: Windows, Linux etc  
  - `python_implementation()` - You should normally expect to see CPython  
  - `python_version_tuple()` - This will return the python version as a tuple (Major, Minor, Patch)    
    `version()` - Not to be confused with the above, system() returns the system release version.  


### Creating your own modules  
- when calling the module, ensure that you have it in any easy to locate directory  
- If the module can't be found, you will receive a `ModuleNotFoundError`  
- once you `import` a module, a `__pycache__` directory is created  
  - There will be a new file created called `<MODULE_NAME>.<PYTHON_IMPLMENTATION>-<PYTHON_VERSION>.pyc`  eg `own_module.cpython-310.pyc`  
  - The file contains python's semi-compiled code for the module (therefore it will be accessed a lot quicker).  
  - When a module is imported, Python will execute the code in it automatically.  
  - Most modules will only contain functions and variable definitions.  
  - Each module is only initialized once.  

- `if __name__ = '__main__'` : Each module has a special variable created by Python. Python sets this variable and it depends on how the variable is run.  
  - If the file is run directly, the `__name__` variable is set to `__main__`, when a given file is _imported as a module_, the name variable is set to the module's **filename.**  
  - A use case, is if you run the module as `__main__`, you could have automated tests fire off, else it assists any code in `main.py`  

### Public and Private variables  
- There is no real way for Python to hide variables from a user of a module, do this but coders follow a convention.  
- if you start a variable name with a single or double underscore `_` or `__`, then that variable should not be modified by a user of the module.  

### Misc  
- Good idea to include the shebang at the top, eg `#!/usr/bin/env python3`  
- Add a docstring `"""blah blah"""` at the top to explain what is going on, a lot of Python tools recognise this docstring automatically.  

### Module Locations and sys.path  
- Two modules can be imported into Python:  
  - `System` - Python checked a variable named sys.path to know which directories to check.    
  - `Custom` or USer created modules - This is located in the same directory as your main code.  
- Python searches the locations in `sys.path`. Refer to the example named `sys-1.py`  
- If Python finds a module, even though it might reside in mulitple locations, it will stop searching and use the first one found.  
- You can append a location to the `sys.path` list by using `sys.path.append('secret')`  
- `sys.path` is just a standard python list and therefore you can use the same methods (eg `.append()` or `.insert()`)that are available with standard lists. Refer to sys-2.py  
- Ensure when adding to sys.path that the module you want to import is after the append/insert operation on the list. Refer to sys-2.py  
- You can use two types of paths:  
  - Absolute paths: Defined completely ('C:\\Users\\UserName')  
  - Relative Paths: Relative to the main file  
    - if the directory is a child of the current directory, simply add it ('secret')  
    - if it is one level higher, add it using relative path notation ('..\\over_here')  

### Using Packages in Python  
- A package is a container or a box for similar modules.  
- Packages can be divided into categories.  
- You can create directories that contain packages and then sub-directories are considered sub-packages. Refer to the project_modules directory in the repo for an example.  
  - There is a `project_modules` **package**  
    - The `communication`, `core` and `messaging` directories are **sub-packages**  
      - In the communication package, there is a **module** named `com`  
      - In the messaging package, there are two **modules** named `event` and `queue`  
      - In the core package, there is a **module** named `util` and there is also a **sub-package** named `additional` which contains a **sub-module** named `security`  
  - To import a module, using the following convention:  
    - `import project_modules.communication.com` This line imports the project_modules package, then the communication sub-package and finally the com module  
    - To use a function `com_func()` in the com module, you call it as follows: `project_modules.communication.com.com_func()`  
    - Alternatively, you could import the module as follows: `from project_modules.communication.com import com_func` and you can call the function simply in your code `com_func()`
- Python does not recurse package directories for modules, therefore, "import project_modules", will not import all sub-packages or modules.  
- `__init__.py` is used to inialise the package if this is necessary, executed by python when one of the package module are imported.  
  - If this file is empty, python will simply ignore it.  
  - This is an optional file in recent Python versions. You needed this file in previous versions (before 3.3) of Python and if left out, Python wouldn't the directory as a package.