## Python Essentials 2  
### Module 1.1    

<ins>Modules, Packages and PIP</ins>  

Topics  
- importing and using Python Modules  
- using standard Python Library modules  
- constructing python packages  
- Using PIP (Python Installation Package)  
  - install, uninstall and using PyPI packages  


`Decomposition` is when you break down larger tasks into smaller ones. `Modules` are used to when splitting larger tasks into smaller ones.  

A `module` is a file **containing Python definitions and statements**  
The handling of modules consists of two different issues:  
- when you want to use a module that you create or was written by someone else. In this case you are the module's `user`  
- when you want to create a brand new module, then you are referred to as the module's `supplier`  

*An analogy:*  
- _books_ are like Python `module` files  
- _shelves_ are the `folders`  
- Each _book_ consists of chapters or in the case of a python module, `entities`  
- Entities are `functions, variables, cconstants, classes and objects`.  
The Python Standard Library can be found here: https://docs.python.org/3/library/index.html  
The Python Module Index can be found here: https://docs.python.org/3/py-modindex.html  (this is a community-driven directory)


### Importing Modules  

- `import` is the keyword, any **import** statements need to be in the code _before any of the module's entities are used_.  

```
import math
import sys
```
is the same as  
`import math, sys`

`namespaces` are spaces in which names exist, are unique and don't conflict.  
importing a module means that you stil need to reference it's namespace first before using the entity.  
eg `math.pi` or `math.cos(0)`  

- `from`, when using the keyword from, the entities are accessible **without qualification!**  
  `from math import sin, pi`, you can then use it as follows (without qualification) `print(sin(pi/2))`  

- **Precedence** of entities with the same name but different definitions; the priority is the last defined entity supersedes the previous definition of the entity (within that namespace).  
  Refer to `2a.import.py` and `2b.import.py`  

- `from math import *` This is a more aggressive approach to import all the entities of a module, it's not recommended.  
  Strong possibility of name conflicts  
  _To get a list of entities in a module use_ `dir(MODULE_NAME)` _e.g.,_ `dir(math)`  

- `as` if you would like to use a different reference to the module entities, in the case of really long module names or if an entity exists with the same name already, it might make more sense to use `as`  
  - `import MODULE as ALIAS` e.g., `import math as m` then you can use it like this `print(m.pi)`  
  - as can also be used to import and rename specific entities, eg `from math import pi as PI, sin as sine`. Refer `3.import.py`  

<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-88  

- *Exercise 3* think broadly  


### Module 1.2  
#### Selected Python Modules

- `dir` using dir will only work when the module has been imported as a whole, that is with `import MODULE_NAME`. Refer to `4.import.py` (the name can also be aliased)  
  be mindful of some of the functions available in modules.  

**math**  
  - trigonometry  
    `cos(x)`, `sin(x)` and `tan(x)` all use a single argument in radians (same goes for `acos(x)`, `asin(x)` and `atan(x)`)  
    there is also the hyperbolic equivalents `cosh(x)`, `sinh(x)`, `tanh(x)`, `acosh(x)`, `asinh(x)` and `atanh(x)`  
    `pi` is a constant  
    `radians(x)` converts radians to degrees and similarly, `degrees(x)` converts from degrees to radians.  
  - exponentiation  
    `e` is a constant  
    `exp(x)`, `log(x)`, `log(x, b)` - b is the base, `log10(x)` - same as log(x, 10), `log2(x)` - same as log(x, 2)  
`pow(x, y)` - x to the power of y  <-- **This does not need to be imported!**  
  - `ceil(x)` - the smaller integer greater than or equal to x  
  - `floor(x)` - the largest integer less than or equal to x  
  - `trunc(x)` - drops the decimal portion of x  
  - `factorial(x)`  
  - `hypot(x, y)` - which is equivalent to `sqrt(pow(x, 2) + pow(y, 2))` but with more precision.  

**random**  
Returns pseudorandom numbers  
The algorithms used to generate the random numbers are deterministic and predictable.  
The number generator takes a value, named the `seed`. Sooner or later the seed values repeat.  
To modify the seed, you take use a number taken from the current time/date.  
  - `seed(x)` - starts with a seed x to generate random values.  
  - `random()` - generates a random value  
  - `randrange(end)` from 0 to end, not inclusive.  
  - `randrange(beg, end)` from beg to end, where end is not inclusive.  
  - `randrange(beg, end, step)` from beg to end, where end is not inclusive.  
  - `randint(left, right)` both are inclusive.  
  There are also other functions that can take arguments such as a list  
  - `choice(sequence)` - picks a number from the provided sequence  
  - `sample(sequence, elements_to_choose)` - returns a list of specified elements, **elements are unique**  

**platform**  
Allows you to interrogate the underlying platform, this includes, the Python information, OS version or hardware information.
  - Refer to the examples in `7.platform.py`  

<ins>Refer to the summary section</ins>
https://edube.org/learn/pe-2/section-summary-89  

### Module 1.3  
#### Modules and Packages   

Summarising some important items:  
- a module is a kind of container filled with functions  
- it's best to include only related functions in a module
- put your modules in groups (aka packages)
- a **package** is basically a directory or folder containing all the modules

Heirarchy is Package -> Module -> Function  

When you create and run a py file that contains an import module command, Python will create a `__pycache__` folder. Python semi-compiles the file, making execution faster.  
Inside the folder will be a file with the name `<NAME_OF_MODULE>.cpython-<X><Y>.pyc`  
  **NAME_OF_MODULE** is the name of the imported module  
  where **X** and **Y** are the Python version numbers, e.g., module.cpython-310.pyc  
  **pyc** stands for Python Compiled  
Python will recompile the `__pycache__` folder if the module changes.  

When a module is imported, the content is **implicitly executed by Python**. This is like an initialisation and only occurs **once**.  
Python will only ever import the module once, even if there is an import defined in multiple locations for the same module.  

Refer to `first_module/main.py` and `first_module/module.py` when considering the following execution examples below  
```
root@4f90959b17d2:/python-institute/pcap/modules# python3 main.py
I like to be a module.
The value of __name__ is: module
root@4f90959b17d2:/python-institute/pcap/modules# python3 module.py 
I like to be a module.
The value of __name__ is: __main__
```  
If you run the module directly, the value will be `__main__` else if it is imported via `main.py`, it will be `module` or whatever the filename may be! **This is an important distinction.**  

Refer to the `second_module/` directory for another example.  

- Modules and Packages in alternate directories  
  Python uses `sys.path` to store directory locations that python uses to search for modules. They are searched in the order that they appear in the list.  
  **zip** files can also be treated as directories.  
  You can traverse the list values using the following `for p in sys.path: print(p)`  
  Say we have the following directory structure  
  `/home/py/modules/modules.py` and `/home/py/code/main.py`  
  You can simply append to the sys.path list as follows: `sys.path.append("/home/py/modules")` or in windows `sys.path.append("..\\home\\py\\modules")`. You can also use `insert()`    
  Once the path is appended, you can simply import the module as follows `import module`  

**Packages**  
When you have a directory structure laid out, you need a file `__init.py__` to make up the package.  
Refer to `8.main2.py` and `9.main2.py` for some examples.  
- A `module` is designed to couple together related entities (functions, variables, constants etc).  
- A `package` is a container which enables the coupling of several related modules under one common name.  
- During the first import a `__pycache__` file is created with a semi-compiled pyc file.  
- `Private entities` need to be prefixed with a `_` or `__`, this is a convention only.  
- `shebangs` are used to instruct the OS what to do with the file.  
- `append` or `insert` custom directories which house packages and modules into the `sys.path` variable.  
- `__init__.py` must be present when importing a package. It is used to initalise the package and/or sub-packages. It can be empty.  


<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-90  


### Module 1.4  
#### Python Package Installer  

To maintain accessibility and usability, there are two things that need to be in place: **a centralised repository** and a tool that allows users to **access the repository**  
The repository name is `PyPI` short for **Python Package Index**, this is maintained by the **Python Working Group** as part of the **Python Software Foundation**  
You can also create your own repo, if you so wish, eg Artifactory  
The PyPI repo is often times referred to as the **Cheese Shop**  

The tool to access PyPI is `pip` short for **pip installs packages**  

There are two ways to install pip on linux:  
- Using something like _apt_ - **recommended**  
- using internal Python mechanisms  

**Dependecies are a phenomenon that appears everytime you're going to use a piece of software that relies on other software**  
Fulfilling all subsequent requirements based on parent requirements is called `dependency hell`. _Pip_ resolves the dependencies for you.  

<ins>Using Pip</ins>  

- `pip3 help`                     - brings up the help menu  
- `pip3 help <operation>`         - will give you information about that specific operation  
- `pip list`                      - lists all the packages that have been installed, giving the package and the version    
- `pip show <package_name>`       - will provide a verbose description of the package, from metadata within the package  
- `pip search <any_string>`       - (case sensitive) will search PyPI for _package names_ and the _package summary strings_. Not supported in the latest pip version, use https://pypi.org/search instead.  
- `pip install --user <pkg>`      - will install the package only for that specifc user  
- `pip install -U <package_name>` - will update the package to the latest, you can also use `--upgrade`  
- `pip install <package_name>==<package_version>` - will install a package at the requested version, e.g., `pip install pygame==2.3.0`  
- `pip uninstall <package_name>`  - to uninstall a package, will ask for confirmation  


<ins>Refer to the section summary</ins>  
https://edube.org/learn/pe-2/section-summary-91  

Quiz 90%  
Test 94%   