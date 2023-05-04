## Python Essentials 2  

<ins>Object Oriented Programming</ins>  

In this module:  
- Basic concepts of object-oriented programming (OOP)  
- The differences between the procedural and object approaches (motivations and profits)  
- Classes, objects, properties, and methods;  
- Designing reusable classes and creating objects;  
- Inheritance and polymorphism;  
- Exceptions as objects.  


### Module 3.1  
#### The foundations of OOP  

Fundamentally, there are two approaches.  
 - Procedural  
 - Object  

The procedural approach has data and code as separate objects.

- The object approach combines the data and code into a set of objects called **classes**.  
  A **class** is like a recipe and can be used twhen you want to create a useful object.  
  Every **object** has a set of traits called **properties** or **attributes** and is able to perform a set of activities called **methods**.    

  The new classes inherit properties and methods fro the originals and usually add some new ones, creating new and more specific tools.  

  Objects are incarnations of a class.  

- Classes  
  Take an example, if Vehicle is the `superclass`, then water vehicle, road vehicle are `subclasses`.  
  Also note that each subclass is more speicalised and the superclass is more general.  
  A class can have more than one superclass.  

- Object  
  An object is the **incarnation of the requirements, traits, and qualities assigned to a specific class**.  
  An object has the following:  
    **name** - a name that uniquely identifies it whithin its home namespace. (noun)
    **properties** - a set of individual properties (it's possible that some objects have no properties at all) (adjective)  
    **method** - a set of abilities to perform specific activities (verb)  
  Creating an object is called an **instantiation**, or an **instance of the class**  


- Inheritance  
  Any object bound to a specific level of a class hierarchy inherits all the traits (as well as the requirements and qualities) defined inside any of the superclasses.  

**Remember that creating a class does not mean that any of the compatible objects will be automatically created**. You MUST create the object.  

The simplest class:  
```
class TheSimplestClass:
    pass
```

To create the object, invoke the class:  
`my_first_object = TheSimplestClass()`  


<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-100  



### Module 3.2  
#### The Stack Example  

A stack is a structure developed to store data in a very specific way.  

An alternate name for a stack is LIFO (Last In - First Out)  
A stack has two operations: `push` and `pop`  

Refer to `1.stack.py` for the procedural approach.  

Some disadvantages of the **procedural approach**:  
  - You might need more than one stack.  
  - Someone can assign values to the stack outside the functions.  
  - To implement other conveniences might become difficult when trying to work with multiple stacks!  

The **objective approach** advantages:  
  - `encapsulation` - Ability to hide or protect selected values against unathorised access.  
  - You can create or instantiate multiple objects and code does not therefore need to be copied or replicated.  
  - Easy to add new functions via inheritance.  

- Creating the stack class (Refer 2.stack.py, 3.stack.py and 4.stack.py)  
  **Constructor**  
  - A class requires a constructor to implement it's properties. 
  - A constructor is required.  
  - The constructor's name is `__init__`   
  - The constructor needs to have at least one parameter.  
  - The parameter is usually named `self` but doesn't need to be, it can be anything you like.  
  - The constructor is defined as `def __init__(self):` and this is run everytime an object is created from the class.  
  
  **Encapsulation**  
  When creating a class, you can use `__` to make a property private (this is a convention only)  
  If you try to access the object property without the `__` you will get an `AttributeError`  

When creating methods inside the class, it must always have `self` as the first parameters, this allows the method to access the entities (properties and methods) in the actual object.  

**A method is obligated to have at least one parameter, which is used by Python itself!**  

- Class using another class  
  Refer to `8.class.py`  
  Python needs you to explicitly call another class' constructor. If you don't, you don't inherit the properties from that classes constructor.  
    This is the only time you can call another class' constructor
    - **note:** invoking any method (including constructors) from outside the class never requires you to put the self argument at the argument's list 
    - Invoking a method from within the class demands explicit usage of the self argument, and it has to be put first on the list.

- Overriding  
  - **If you add the same function name to a subclass, then the superclass function is overridden**  


<ins>Refer to the summary section</ins>
https://edube.org/learn/pe-2/section-summary-101



### Module 3.3  
#### OOP Properties  

In general a class can be equipped with two different kinds of data to form a class property.  
This type of class property exists when and only when it is explicitly created and added to an object! This is done during the object initialisation in the constructor.  
  Moreover, it can be done in any moment of the object's life ..and.. and existing property can be removed at any time!  

Such an approach has some important consequences:  
  - Different objects of the same class **may possess different sets of properties**.  
  - There needs to be a way to **safely check if a specific object owns a property** that you want to utilise.  
  - Each object **carries its own set of properties**  

These variables (properties) are called **instance variables**  

- **Instance Variables** (Refer to `9.instancevaraible.py` and `10.instancevariable.py`)  
  They are tied closely to the instance itself and not the class.  
  To see which properties/variables a object has, you can use the `__dict__` property to see them. It's quite handy!  
  Modifying an instance variable on any object has no impact on all the remaining objects. It only affects the current object possessing that "new" property.  
  Instance variables are perfectly isolated from each other.  
  You can make an instance variable private.  
  When printing the `__dict__` of an object and it contains private variables, Python **mangles** the the name, eg `_ExampleClass__firstvar`. Class Name then variable name. 
    **If you add a private variable outside the class code, then the variable will not be mangled!**   
  You can still access a private variable outside of the class using something like this: `print(example_object_1._ExampleClass__first)`  

- **Class Variable** (Refer to `11.classvariable.py` and `12.classvariable.py`)  
  A class variable is a **property which exists in just one copy and is stored outside any object**.  
  A class variable exists in one copy even if there are no objects in the class.  
  A class variable **aren't shown** in the `__dict__` property.  
  A class variable always presents the same value in all objects (class instances).  

- `__dict__` - refer to `14.classvariabletest.py`  
  You can use this to see the properties of a class or an object.  
  If you use it on the class, you will see any class properties.  
  **NOTE** `varia`, `self.varia` and `ExampleClass.varia` are all entirely different and independent variables!!! They can be treated as individual variables that aren't related at all.  

- Checking that an attribute exists  
  Compared to other programming languages **you may not expect that all objects of the same class have the same sets of properties**.  
  Refer to `15.check.py` to see that when referencing a non-existant object (class) attribute, you get an `AttributeError`  
  To check for the existence, you can use a `try..except` block but isn't recommended (refer `16.check.py`), the best approach is the `hasattr()` function!  
  `hasattr()` function is able to check if any object/class contains a specific property!  
    This function requires two parameters:
      - the class or object name
      - the name of the property that you would like to check, **it needs to be a string**  
  Refer to `17.check.py` to see `hasattr()` in action.  


<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-102   



### Module 3.4  
#### Methods  

