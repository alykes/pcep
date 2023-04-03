## Object Oriented Programming  

This module will cover OOP conventions in Python

### Introduction  

There are four main OOP principles, they are:
- Encapsulation  
- Abstraction  
- Inheritance  
- Polymorphism  

#### Procedural Programming
Procedural programming has been used up til now. Good for small programs done quickly.  
Procedures in the Python language would be considered functions (which are a series of steps to be carried out).  
Procedural Approach is about using functions that do something with data.  
The functions no nothing about the data.  
No restrictions, any function can call any other function and work on any data.  

#### OOP
- OOP tries to eliminate some of these issues.  
- In OOP, data and functions are kept together, in objects.  
- An object is a structure that has some data in the form of traits.  
  - These traits are called properties, attributes or fields.
  - Objects are able to invoke some functions in the form of methods.  
  - Objects interact with each other.  

### Objects and Classes  
- Classes are templates used to create objects  
- Classes contain two types of entities:  
  - `Attributes` - which are like variables.  
  - `Methods` - Which are like functions.  
- We instatiate objects from classes, instances are therefore objects of the class.  
- Can't create an object if there is no class but you can create a class and never instantiate an object from it.  
- Each class has:  
  - A `name`  
  - A set of `properties`  
  - `methods`  
- A class name starts with a capital letter (by convention)  
- Use a `constructor` to construct objects of a given class, the constructor definition is a function called `__init__`  
  - `def __init__(self):` this is the constructor, Python only uses this for constructing the object.  
  - All Python constructors must have at least one parameter, use the `self` parameter as a convention.  

### Encapsulation and Abstraction  
- Encapsulation states that `objects` should keep their state `private`.  
- Only expose a set of functions to the outside world and not everything.  
- Encapsulation is the use of private properties, such as `__speed` in example `class-4.py`  

- Abstraction states that the objects should keep the details of how they work to themselves and only expose some high level operations to the outside world.  
- Basically like a black box, the details are abstracted from the user.  
- The details of when you call the methods in a class are abstracted away from the user.  

### Instance Variables  
- Objects of the same class can have different properties!  
- Each object has its own set of properties with its own values.  
- Properties of one object do not interact with those of another object.  
- These properites are called `instance variables`  
- A way to check what the instance variables are set to, is to use `__dict__`. Refer to `invar-1.py`  
- Once you set a variable to private by using `__`, the object name will become **mangled** (aka **Name Mangling**)when using `__dict__`, refer to `invar-2.py`  
- You can still use the mangled name outside the class definition to access that private property in an object.  
- The double underscore is more of a convention, there is no formal way to stop someone from access the private properties.  
- Adding a private property outside the class will not mangle the property. refer `invar-2.py`

### Class Variables  
- A property that exists in just one copy, it exists in the class itself but outside any object.  
- It doesn't use `self`  
- To access the class variable, you need to use the class name followed by a dot `.` eg `Dog.counter` Refer to `classvars-1.py`  
- The class variables do not show up in `__dict__` of the object as it is a class variable, not an instance variable!  
- You can access the class variable directly. eg `print(Dog.counter)` Refer to `classvars-1.py`
- Class variables can also be made private and the name will also be mangled. 
- You can also use `__dict__` on a class.  
- `hasattr()` is used to check if an attribute exists in a **class** or **object**. Pass the object and then the property. Refer to `classvars-3.py`  
- `__name__` will return the name of the class  
  - can be used with an object in the form of `print(type(my_pet).__name__)` to return the type, refer to `classvars-4.py`  
- `__module__` - returns the name of the module that contains the definition of the class. `print(Dog.__module__)` will return `__main__`

### Instance, Class and Local Variable Comparisons  
Refer to the example icl.py  

### Methods  
- A method is a function inside a class.  
- Each method must have at least one parameter.  
- You cannot use a return statement in a constructor. It returns your object and nothing else!  
- Methods can be private like properties, add a `__` and the method will be `mangled`.  
- You can override the defualt behaviour or printing an object `def __str__(self):` Refer to `meth-1.py`  
  - One parameter, `self`, and returns one value only.  

### Reflection and Introspection  
- `Introspection` is the ability of a program to **check** the type of an object or its properties at **runtime**.  
- `Reflection` is the ability of a program to **change** the properties or methods of an object at **runtime**.  
- Take a look at the example `reflint-1.py`, particularly the `empty_strings()` function.

### Inheritance  
- When one object or class is based on another object or class. This allows for the creation of additional class types:
  - Super Class - Broader and more general.  
  - Sub Class - Detailed and concrete.    

Example  
Where `Vehicle` is the highest level, then there are two sub categories, `Land` and `Water`. Land is split further into `car` and `motocycle`, whereas water has one type, `boat`.  
== Vehicle ==  
== Land Vehicle ==              == Water Vehicle ==  
== Car ==   == Motorcylce ==        == Boat ==  

We can say that `Land Vehicle` is a `Super Class of Car`, `Vehicle` is a `Super Class of Car` also. `Car` would then be a `sub-class of Land Vehicle`. Refer `inh-1.py`  
**Note** that classes are also sub-classes of themselves!  

#### Inheritance Properties  
- Refer to `inh-2.py`, `inh-3.py`, `inh-4.py`, `inh-5.py` for some examples  

#### Inheritance of class variables and methods  
- Refer to `inh-6.py` for some examples  

#### Overriding properties and methods  
- Anything definied in the class that is being called will override the exact same method and variable names in the super classes.  
- Python first tries to find the entity in the class itself before looking elsewhere, like a superclass.  
- It will look for the entity in the inheritance chain from bottom to top (with the most general class at the very end)  
- Method overriding helps achieve one of the 4 core components of OOP, `Polymorphism`  
- Refer `ovr-1.py` and `ovr-2.py`  

#### Polymorphism  
- Is the ability of different classes to take different forms. This is generally done via `method overriding`!  
- Refer to `ovr-3.py` to see how a function changes the behaviour of a superclass `polymorphism`  
- A function or method behaves differently based on the object that calls it.  
- Refer to `ovr-4.py`, when mehtods use other methods.  
- Python will always try to find a matching method within the object itself!  

#### isinstance - is
- Refer to `isin-1.py` for some examples in relation to objects.  
- `isinstance()`  
  - Checks to see if the object is an instance a given class.  
  - Also returns True if the object was created with a subclass of the class that is being checked.  
- `is`  
  - is an operator that is used between two variables.  
  - REMEMBER, object variables contain a reference to the object in memory, not the object itself.  
    - The variables below point to the same object! They are essentially equal.  
      ```
       my_vehicle = Vehicle(60)
       my_new_vehicle = my_vehicle
      ```
  - `print(my_vehicle is my_new_vehicle)` # True => because they point to the same object.  
- Refer to `is-1.py` for examples of using is against primitive data types.  
  - `integers`, is will behave like a == operator.  
  - `strings`, depending on how the string was created, Python will either point to the same object if the variables were created the same way, or to different objects. Refer `is-1.py`  

### Multiple Inheritance  
- When a class has more than one Super Class.  
- When a class inherits from more than one Super Class.    
- Syntactically, all you do is provide all the classes separated by commas.  
- Easy to lose track of properties or methods that are inherited.  
- Refer to `multinhe-1.py`, `multinhe-2.py`, `multinhe-3.py` for some examples.  
- `MRO` (Method Resolution Order) is used:  
  1. Look inside the object first.  
  1. If not found, look in the superclass from the left to the right.  
  1. If not found, show an error.  
- AVOID using multiple inheritance, use it as a last resort.  

### __bases__ property  
- Returns the base classes that the given class inherits from. Refer to `bases.py`  
- If there are no inheritence classes, then the resulting tuple will be `(<class 'object'>,)`  

### Diamond Problem  
- This is what we discussed above with multiple inheritance. Where the inheritance diverts and points back to a point at the top `D -> C and B`, `B -> A` and `C -> A`.  
- The resolution to the Diamond problem in Python is to use MRO or Method Reslotion Order.  



### EXAM TIP  
Can you have a default value for the self constructor parameter?  
**Answer:** Yes but it will be ignored by Python!  

```
class Car():
  def __init__(self='default value', speed=100):
    self.speed = speed
 
my_toyota = Car()
print(my_toyota.speed)   # default value for self ignored
```