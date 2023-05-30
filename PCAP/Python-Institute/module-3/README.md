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

_Definition:_  
In it's simplest definition, a method is simply a function embedded in a class.  

There is one fundamental requirement, **a method is obliged to have at least one parameter**.  
The first parameter is usually named `self` and this convention should be followed.  
When invoking the method outside the class, don't provide the `self` parameter.  
Any parameters need to be placed after `self` in the class definition.  

- `self`  
  - The `self` parameter is used `to obtain access to the objects's instance and class variables`.  
    Refer to `23.self.py` for an example.  
  - The `self` parameter is also used `to invoke other object/class methods from inside the class`.  
    Refer to `24.self.py` for an example.  

- `__init__` constructor (refer to `24.constructor.py`)  
  - if you name a method this, it will be the class constructor.  
  - If a class has a constructor, it will be invoked automatically and implicitly when the object of the class is instantiated.  

  The constructor:
    - Is **must have the** `self` **parameter**
    - **may, but doesn't need to, have more parameters** than just `self` 
    - **can be used to set up the object**, it initialises the internal state of objects that use the class.  
    - The constructor **cannot** return a value.  
    - **cannot be invoked directly either from the object or from inside the class**, although you can invoke it from an object's subclass.  

  As `__init__` is a method, and a method is basically a function and you can do the same tricks that you do with constructors/methods as you do with ordinary functions.  
  refer to `26.constructor.py`  
  **Property name mangling** also _applies to methods as well_, refer to `27.mangle.py`  

- **The inner life of classes and objects**  
  Each Python class and object is pre-equipped with a set of useful attributes.  
  One of them is the `__dict__` property.  
  - The `__dict__` property:  
    - Stores a dictionary of the properties.  
    - on the object only shows the variables.  
    - on the class it shows the class variables and the class methods.  
    - In example `28.dict.py` you can see how this.  
  - The `__name__` property:  
    - Stores a string  
    - The `__name__` property contains the **name of the class**.  
    - Handy if you want to find the class of a particular object, in combination with `type()`  
    - refer to `29.type.py`    
  - The `__module__` property:  
    - Stores a string  
    - It returns the **module name that contains the definition of the class**.  
    - `__main__` is common to see when you have created the class in the **file that is currently being run**  
  - The `__bases__` property:  
    - Stores the classes, _not class names_, of the direct **superclasses** for the class in a tuple.  
    - The order they are stored in is the same as the class definition.  
    - **NOTE** only classes have this property, objects do not!  
    - **NOTE** A class without an explicit superclass points to **object**, _a predefined Python class_, as its direct ancestor.
    - Refer to `30.bases.py`  

- **Reflection and Introsepction**  
  - **introspection** is the ability of a program to examine the type of properties of an object at runtime.  
  - **reflection** is the ability of a program to manipulate the values, properties and/or functions of an object at runtime.  
  - Both reflection and introspection enable a programmer to do anything with any object, no matter where it comes from.  
  - A perfect example of this is `31.investigation.py`  


<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-103  



### Module 3.5  
#### Inheritance  

- `__str__()`  
  - First you need to understand how an object **presents** itself. Refer to `33.present.py`  
  - When you put an object in a `print()` statement, you can use a class method named `__str__()` to produce a customised result. Refer to `34.present.py`  

- inheritance is a common practice of **passing attributes and methods from the superclass (defined and existing) to a newly created class, called the subclass.**  
  It's basically **a way of building a new class, not from scratch, but by using an already defined repertoire of traits**.  
  So we say that the new class, inherits everything and is then able to add new methods and properties.  
  You can therefore build more specialised `concrete` classes.  
  Inheritance is fully transitive! **Note:** if `B` is a _subclass_ of `A` and `C` is a _subclass_ of `B`, this also means that `C` is a _subclass_ of `A`!   
  Refer to `35.inheritance.py`  

- `issubclass(ClassOne, ClassTwo)` - This function offers the ability to identify a relationship between two classes. It can check whether a class is a subclass of another class.  
  - Will return `True` if **ClassOne** is a subclass of **ClassTwo**   
  - **NOTE** Each class is also considered to be a subclass of itself!  
  - Refer to `36.subclass.py` for an example.  

- `isinstance(ObjectName, ClassName)` - Checks to see if an object is an instance of a class (or superclass).  
  - Returns `True` if `ObjectName` is an instance of `ClassName`.  
  - Note that inheritance also determines if the instance is inheriting a **superclass** and will return **True** if it is.  
  - Refer to `37.instance.py` for an example.  

- `is` operator, this is used to check whether two variables refer to the same object. Such as `object_one is object_two`  
  - Important to note that the variables do not store the object themselves but **only handles pointing to the internal Python memory of the object**.  
  - variables that are assigned objects, do contain the actual object but rather a pointer to the location in memory where the object is stored, that is why variables can point to the same object.  
  - Refer to `38.is.py` to see how `is` works when checking objects.  

- A look into how Python inherits methods. In particular how a subclass calls the constructor of the superclass.  
  - refer to `39.construct.py`  

- `super()` function is quite handy as it allows you **to access any of the superclass resources** without needing to know the name of the superclass.  
  - So you could write `super().__init__(name)` instead of `Super.__init__(self, name)`  
  - Note that you don't need to pass **self** to the function and can therefore invoke the constructor using one argument.  
  - Refer to `39.construct.py` and `40.construct.py` for a practical example.  

- Class variables  
  - Accessing class variables across subclasses and superclasses.  
  - Refer to `41.classvars.py` for different methods of creating and using class variables.  

- A few points on how Python finds properties and methods.  
  When you try to access any object's entity, Python will try (in this order):  
   - find it inside the object itself.  
   - find it in all the classes involved in the object's inheritance line from bottom to top;  
     If both of there fail, then Python will raise an **AttributeError** exception  
  - The following example has a good breakdown of the inheritance line, `42.inheritance.py`  

- **Multiple Inheritance**  
  - Multiple inheritance occurs when you a class has more than one superclass.  
  - Syntactically, this is represented with a comma separated list of superclasses, e.g., `class Sub(SuperA, SuperB)`.  
  - This means that the `Sub` class has **two** superclasses and will inherit all the goods offered by both `SuperA` and `SuperB`.  
  - Refer to `43.multi.py`  

- **overriding**  
  - Remember that Python will look from the bottom up for inheritance, this also goes for overriding!  
  - If there are two superclasses on the line in a class definition, then inheritance and overriding goes from left to right!  
  - Refer to `44.overriding.py` and `45.overriding.py` for examples on two situation that have conflicting entities.  

- **Polymorphism**  
  - This is when the exact same call of an entity behaves in two completely different ways depending on the where the call originated from.  
  - This can occur when the subclass is able to modify its superclass behaviour.  
  - Refer to `46.poly.py` and `47.poly.py`  

- **abstract method**  
  - This is when you don't have any details in a method, except for a `pass` statement or similar.  
  - Basically a place holder with a descriptive method name that will have it's details filled out later.  

- **composition**  
  - Inheritance is not the only way of constructing adaptable classes, you can usually achieve the same goals using the technique named composition.  
  - **Composition is the process of composing an object using other different objects**.  
  - The object used in the composition delivers a set of desired traits (properties or methods). They are like blocks used to build a more complex structure.  
  It can be said that:  
    - **Inheritance extends a class's capabilities** by adding new components and modfying existing ones.  
    - **Composition projects a class as a container** and has the ability to store and use other objects (which are derived from other classes), therefore **each of the objects implements a part of the desired class's behaviour**.  
    - Take a very good look at the example.  
    - THIS IS A TOPIC THAT NEEDS A BIT OF EXTRA EFFORT. Refer to `48.composition.py` for an example.  

- **Single Inheritance vs. Multiple Inheritance**  
  Note:  
    - a single inheritance class is always simpler, safer, and easier to understand and maintain;  
    - multiple inheritance is always risky, as you have many more opportunities to make a mistake in identifying these parts of the superclasses which will effectively influence the new class;  
    - multiple inheritance may make overriding extremely tricky; moreover, using the `super()` function becomes **ambiguous**;  
    - multiple inheritance violates the single responsibility principle as it makes a new class of two (or more) classes that know nothing about each other;  
    - **we strongly suggest multiple inheritance as the last of all possible solutions** - if you really need the many different functionalities offered by different classes, composition may be a better alternative.  

- **MRO** (Method Resolution Order)  
  - MRO, in general, is a way (you can call it a strategy) in which a particular programming language scans through the upper part of a class’s hierarchy in order to find the method it currently needs.  
  - refer to `49.mro.py`  

- **The diamond Problem**  
  - there is the top-most superclass named A;  
  - there are two subclasses derived from A: B and C;  
  - and there is also the bottom-most subclass named D, derived from B and C (or C and B, as these two variants mean different things in Python)  
  - multiple inheritance is allowed but MRO is always in charge!  
  Refer to `50.diamond.py` to see it expressed as Python code.  



<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-1-2-8  
https://edube.org/learn/pe-2/section-summary-2-2-11  



### Module 3.6  
#### More About Exceptions  

The **try..except** block can also have another branch named the `else` branch.  
The `else` branch is executed only when no exception has been raised inside the `try:` part of the block.  
So we can say that exactly one branch can be executed after a `try:`, that is one beginning with `except:` or one starting with `else:`.  
An `else:` branch **must** be placed after an `except` branch.  
Refer to `52.else.py`  

The **try..except** block can also be extended by one more branch, `finally:`.  
It **must** be the last branch.  
`else:` and `finally:` can co-exist.  
`finally:` is **ALWYAS** executed, if there was or wasn't an exception, it is still run!  

**Exceptions are classes**. When an exception is raised, an object of the class is instantiated!  
The `as` keyword is used to place the exception object in a variable, normally `e`, that is,  `except Exception as e:`  
The identifiers scope only covers its `except` branch and doesn't go any further.  
Refer to `54.exceptions.py` for an example.  
Refer to `55.ex.tree.py` for a list of all the exceptions in a tree like output.  

**Anatomy of Exceptions**  
The `BaseException` class introduces a property named `args`.  
`args` is a tuple designed to gather all arguments passed to the class constructor.  
  If it's empty, the constructor is invoked without any arguments.  
  Refer to `56.arg.ex.py` to see an elegant way of printing the `args` property.  

**Creating your own exception**  
You would create your own exceptions if you want to extend on the already existing ones.  
You **define your own, new exceptions as subclasses derived from predefined ones**.  
Depending on how narrow or broad you want your exception to be, you can derive it from say `Exception` for a broad exception type.  
Refer to `57.defined.ex.py`  
To create an exception classes from scratch, the most important things are to:  
  - define the superclass  
  - define the constructor  
Refer to `58.defined.ex.py`  


<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-104  

Quiz 90%  
Test 88%, 100% error on Exception and overwriting self.args in a class. Other was superclass constructor invocation.  

