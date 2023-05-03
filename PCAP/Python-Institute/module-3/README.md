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

- Instance Variables  
