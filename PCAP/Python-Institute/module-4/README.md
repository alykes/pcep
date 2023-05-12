## Python Essentials 2  

<ins>Miscellaneous</ins>  

In this module:  
  - Generators, iterators and closures;
  - Working with file-system, directory tree and files;
  - Selected Python Standard Library modules (os, datetime, time, and calendar.)



### Module 4.1  
#### Generators  

- `Generator` is a specialised code able to produce a series of values, and to control the iteration process. **Generators** are often called **iterators**, although there are subtle differences.  

Take a look at the following snippet:  
```
for i in range(5):
  print(i)
```

The `range()` function is in fact a **generator**.  

Differences between a function and a generator:  
  - A **function** will return _one value_  
  - A **generator** will return a _series of values_ and is (implicitly) invoked more than once!  

In the code snippet above, the `range()` function is invoked six times, providing subsequent values from 0 to 4, before signaling that the series is complete.  

- **The Iterator Protocol** is a way in which an object should behave to conform to the rules imposed by the context of the `for` and `in` statements.  
  - An object conforming to the iterator protocol is called an **iterator**  

An iterator must have two methods:  
  - `__iter__()` which returns the object itself and is invoked once.  
    The `__iter__` method should extract the iterator and entrust it with the execution of the iteration protocol.  
  - `__next__()` which returns the next value of the series, it is invoked by the `for`/`in` staatements in order to pass through the next iteration.  
    If there are no more values, the method should raise the `StopIteration` exception.  
Refer to `1.fibonacci.py` for the `objective` version of the fibonacci number generator.    
To see an example of **composing the iterator into another class** refer to `2.compose.py`  

The iterator protocol can be inconvenient because it brings **the need to sve th state of the iteration between subsequent** `__iter__` **invocations**.  

- `yield` can be considers a smarter version of the `return` statement with one fundamental difference.   
  A traditional function using `return`:  
  ```
  def fun(n):
    for i in range(n):
      return i
  ```
  This function will never complete as return breaks the function before the for loops gets to finish.  
  A function that uses the `yield` keyword:  
  ```
  def fun(n):
    for i in range(n):
      yield i  
  ```
**This function is now a generator! The function also does not lose state!**  
All the variables are frozen in place and don't lose their value, they wait for the next invocation and the execution is resumed (not started from scratch like `return`)  
**Note** -  There is one important limitation, the function **SHOULD NOT** be invoked explicitly, as - in fact - it isn't a function anymore but a **generator object**.  
The invocation will **return the object's identifier**, and not the series that you might expect.  
Refer to `3.generator.py` for an example of invoking a generator.  
Also take a look at the examples in `4.gen.examples.py` to see how to use the generator in various invocations.  
`5.fib.gen.py` shows how to implement the **generator version** of the fibonacci function as compared to the **objective version** in `1.fibonacci.py`  

- List Comprehension Revision  
  Basically a method to create lists and their contents in Python.  
  Refer to `6.list.comp.py`  

- Conditional Expressions on one line  
  `1 if x % 2 == 0 else 0`, basically, the value is 1 if the condition is met or else it is 0.  
  It is not a conditional instruction, it is an **operator**!  
  Refer to `7.cond.op.py`  
  You can also use this trick with list comprehension, the syntax might catch you off guard when you see it for the first time.
  `[1 if x % 2 == 0 else 0 for x in range(10)]` 
  Extending from this, you can create the same list using either list comprehension or a generator, refer to `8.list.comp.gen.py` to see the differences.  
  You can use a method that doesn't save either list to a variable, refer to `9.inplace.py`

- The `lambda` function  
  This is a concept borrowed from mathematics, from lambda calculus.  
  Used to simplify code to make it clearer and easier to understand.  
  Another name for a lambda function is **an anonymous function**.  
  A lambda function doesn't need to have a name but you can name it if you wish.  
  
  - `lambda parameters: expression` <-- This is a decalaration of a lambda function.  
    This returns the value of the expression when taking into account the current value of the current lambda argument.  
    Refer to `10.lambda.py` for some examples of lambda functions and how to use them.    
  
  - How to use lambdas and what are they used for?  
    They are anonymous pieces of code intended to evaluate a result.  
    Refer to `11.lambda.py` for an example of an a function that is a good candidate to turn into a lambda function.  
    Refer to `12.lambda.py` for the refactored code.  

  - `map(function, list)` applies the function passed by its first argument to all its second argument's elements, and returns an iterator delivering all subsequent function results.  
    - The map function takes two arguments:  
      - a function  
      - a list - This may be anything that can be iterated over (a tuple or a generator)  
    - map **can** accept more than 2 arguments!  
    - You can use the resulting iterator in a loop or convert it inta a list using the list() function.  
    - Refer to `13.map.py` for an example.  
  
  - `filter()` - filters its second argument while being guided by directions flowing from the function specified as the first argument (the function is invoked for each list element, just like in `map()`).  
    - filters out elements based on whether or not the condition is met on the element. `True` - Element stays, `False` - Element removed.  
    - It's more easily explained with an example. Refer to `14.filter.py`    

- **Closures**  
  - The defintion: **closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore**.  
  - Refer to `15.closure.py` for an example and an explanation.  
  - A closure has to be invoked in exactly the same way in which it has been decalred. (Same amount and type of parameters)  
  - It's possible to declare a closure equipped with an arbitary number of parameters.  
  - A clsure can also modify it's behaviour by using values taken from outside.  
  - You can create as many closures as you like from one piece of code. Refer to `16.closures.py`  



<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-105



### Module 4.2  
#### Processing Files  

- **File names**  
  Windows uses `\` and linux uses `/`  
  Unix and Linux file names are case sensitive and windows is not.  
  Python is smart enough to convert the `/` to `\` if it's a windows OS.  
  Python uses **handles** or **streams** to communicate with files.  
  
- **File streams**  
  You use `open` and `close` file streams.  
  The way you open a stream and the method it will be processed is called the `open mode`  
  There are two basic operations for a stream:  
    - `read`- read from a stream (read file contents)   
    - `write` - write to a stream (write file contents)  
  There are three basic modes to open a stream:    
    - `read mode` - allows read operations only; attempting to write to a file causes `UnsupportedOperation`, which inherits `OSError` and `ValueError`, and comes from the `io` module.  
    - `write mode` - allows write operations only; attempting to read the stream will cause the same exception as above. 
    - `update mode` - allows both read and write.  

- **File handles**  
  Python assumes that every file is hidden behind an object of an adequate class.  
    An object of an adequate class is **created when you open the file and annihilate it at the time of closing**.  
    In general, the object comes from one of these classes `IOBase` <--[`RawIOBase`, `BufferedIOBase`, `TestIOBase`]  
    We will only be dealing with `BufferedIOBase` and `TextIOBase`  
  All the streams are divided into **text** and **binary** streams.  
    - **text** streams are arranged by lines and the file is written or read mostly character by character or line by line  
    - **binary** streams contain sequences of bytes. The sequence can be an executables, image, audio etc. The data is read/written byte by byte or block by block
  **NOTE** in Unix/Linux, line endings are marked by `LF` or `\n` (ASCII 10), in Windows they are marked `CR` `LF` or `\r\n` (ASCII 13 and ASCII 10)  
    Python will automatically replace `\r\n` with `\n` on a windows system, this is a process called `translation of newline characters`  
    Issues that arise between the systems is called `non-portability`  
    If a program functions the same in both Windows and Linux, it is said to be `portable`  
  If no advisory is set when opening a file, the default will be used, `text mode`  

- **Opening streams**  
  A function is invoked in the following way: `stream = open(file, mode = 'r', encoding = None)` - encoding as in UTF-8 etc.  
    If the _file_ doesn't exist then a `FileNotFoundError` exception will be raised.  
    `mode` and `encoding` may be omitted as they contain default values.  
      The default `mode` is `r` or read in text mode, and the default encoded depends on the system being used.  

- **Stream Modes**  
`r` open mode: read  
  the stream will be opened in **read mode**  
  the file associated with the stream **must exist** and has to be readable, otherwise the `open()` function raises an exception.  

`w` open mode: write  
  the stream will be opened in **write mode**  
  the file associated with the stream **doesn't need to exist**  
  if it doesn't exist it will be created   
  if it exists, it will be truncated to the length of zero (erased); if the creation isn't possible (e.g., due to system permissions) the `open()` function raises an exception.  

`a` open mode: append  
  the stream will be opened in **append mode**  
  the file associated with the stream **doesn't need to exist**  
  if it doesn't exist, it will be created  
  if it exists the virtual recording head will be set at the end of the file (the previous content of the file remains untouched.)  

`r+` open mode: read and update  
  the stream will be opened in **read and update mode**  
  the file associated with the stream **must exist** and has to be writeable, otherwise the `open()` function raises an exception  
  both read and write operations are allowed for the stream.

`w+` open mode: write and update  
  the stream will be opened in **write and update mode**  
  the file associated with the stream **doesn't need to exist**; if it doesn't exist, it will be created; the previous content of the file remains untouched  
  both read and write operations are allowed for the stream.  

- **Selecting text and binary modes**  
  If there is a letter `b` at the _end of the mode string_ it means that the stream is to be opened in the binary mode.  
  If the _mode string ends_ with a letter `t` the stream is opened in the text mode.  
  **NOTE** is the mode is set to `a`, the current file position is set after the last byte of the file. If `a` is **not** set, the current file position is set to before the first byte.  

|Text mode|Binary mode|Description|
|---|---|---|
|rt|rb|read|
|wt|wb|write|
|at|ab|append|
|r+t|r+b|read and update|
|w+t|w+b|write and update|

**Extra Tip** You can also open a file for its exclusive creation. You can do this using the `x` open mode. If the file already exists, the `open()` function will raise an exception.  

Refer to `17.files.py` for a simple example of opening and closing a file.  

- **Pre-Opened Streams**  
  There are three streams that don't need to be preceeded with the `open()` function.  
  They are already opened and don't require any preparation, you just need to `import sys`  
  
  The streams are:  
    - `sys.stdin`  
      stdin - **standard input**  
      the stdin stream is normally associated with the keyboard, pre-open for reading and regarded as the primary data source for the running programs  
      the well-known `input()` function reads data from stdin by default.
    - `sys.stdout`  
      stdout - **standard output**  
      the stdout stream is normally associated with the screen, pre-open for writing, regarded as the primary target for outputting data by the running program  
      the well-known `print()` function outputs the data to the stdout stream.  
    - `sys.stderr`  
      stderr - **standard error output**  
      the stderr stream is normally associated with the screen, pre-open for writing, regarded as the primary place where the running program should send information on the errors that it encounters
      Python haven't presented any method to send the data to this stream  
      the separation of stdout (useful results produced by the program) from the stderr (error messages, undeniably useful but does not provide results) gives the possibility of redirecting these two types of information to the different targets.  

- **Closing Streams**  
  This is the last operation that is performed on a stream, **note**, this does not include `stdin`, `stdout` or `stderr`.  
  This is a method invoked on the stream object: `stream.close()`  
  This function expects **no arguments**  
  The exception raised is an `IOError` if it runs into an error.  
  Most developers trust that the `close()` function always succeeds and thuse there is no need to check if it's done correctly.  
    This isn't always a good idea because it can fail in certain circumstances, e.g., the data is sent to the stream and it's cached or buffered before getting to the actual physical device. If a `close()` occurs, then the operation fails.  

- **Diagnosing stream problems**  
  The `IOError` object is equipped with a property named `errno`.  
  Refer to `18.errno.py` for an example on how to access the it.  

  Some of the selected constants for detecting streaming errors are:  
    `errno.EACCES` → Permission denied  
      The error occurs when you try, for example, to open a file with the read only attribute for writing.  
    `errno.EBADF` → Bad file number  
      The error occurs when you try, for example, to operate with an unopened stream.  
    `errno.EEXIST` → File exists  
      The error occurs when you try, for example, to rename a file with its previous name.  
    `errno.EFBIG` → File too large  
      The error occurs when you try to create a file that is larger than the maximum allowed by the operating system.  
    `errno.EISDIR` → Is a directory  
      The error occurs when you try to treat a directory name as the name of an ordinary file.  
    `errno.EMFILE` → Too many open files  
      The error occurs when you try to simultaneously open more streams than acceptable for your operating system.  
    `errno.ENOENT` → No such file or directory  
      The error occurs when you try to access a non-existent file/directory.  
    `errno.ENOSPC` → No space left on device  
      The error occurs when there is no free space on the media.  

  You can also use `strerror()` from the `os` module to get a descriptive string of the error number that is raised.  
  `strerror()` expects one value, an error code.  
  If you pass a non-existant error code, then the function will raise a `ValueError` exception.  
  Refer to `19.errno.py` (not using `strerror()`) and `20.errno.py` (utilising `strerror()`)  


<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-106



### Module 4.3  
#### Processing Text and Binary Files  

Basic techniques on reading file contents.  
- There are multiple techniques and none is any better or worse than the other, you should be flexible with the one that you use.  

- `read()` This is the most basic function to read the stream. Takes an integer argument and will read that many characters.  
  If this function is applied to a text file then it is able to:  
    - read a desired number of characters (including just one) from the file, and return them as a string  
    - read all the file contents, and return them as a string  
    - if there is nothing more to read (the virtual reading head reaches the end of the file), the function returns an empty string.  
    - Refer to `22.charcount.py`  
    - **NOTE** reading a terabyte-long file using this method may corrupt your OS!  

- `readline()` This method will read the contents of a stream one line at a time.  
  - The method attempts to **read a complete line of text from the file**  
  - **A string is returned** on a successful read otherwise it will return an empty string.  
  - Refer to `24.readline.py`  

- `readlines()` This method will attempt to **read all the file contents and will return a list of strings, one element per file line**.  
  - Not to be confused with `readline()` above, without the `s`.  
  - readlines takes an integer argument, it specifies _how many bytes (characters)_ to read **NOT LINES!!**  
  - It works in a couple of distinct ways.  
    - If the buffer (argument) you specify is smaller than the line, it will read the entire line.  
    - If the buffer (argument) you specify is larger than the line but smaller than the next line, it will only read the first line.  
    - If the buffer (argument) you specify is larger than the line and larger than the next line, it will combine both lines into a single element.  
  - Refer to `25.readlines.py`  

- Trait of the object returned by the `open()` function in text mode.  
  - **The object is an instance of the iterable class**.  
  - The **iteration protocol defined for the file object** is very simple - its `__next__` method just **returns the next line read in from the file**.
  - The object also automatically invokes `close()` when any of the file reads reaches the end of the file!  
  - Refer to `25.open.iter.py`  

- `write()` - Expects just one argument, a string that will be transferred to an open file. _Note:_ writing to a file in read mode won't succeed.  
  - You need to add any new line characters that you would like in the file.  
  - The write function can add character by character to a file as well.  
  - Refer to `26.write.py` for an example.  

- `sys.stderr.write("Some Error Message")` this is to write to stderr, you also need to `import sys`  
  - refer to `27.write.py`  


- **ByteArrays**  
  - Overview  
    - Python has a specialised class to store amorphous data.  
    - **Amorphous data is data which have no specific shape or form** - they are basically just a series of bytes.  
    - Don't think of amorphous data as strings or lists because they are neither.  
    - The specialised class that Python uses is named **bytearray**.  
    - A **bytearray** is a array containing (amorphous) bytes.  
    - You need to invoke the creation of a bytearray object if you would like to read or process any amorphous data.  
      - To create such a container, you can use the following bit of code:  
        `data = bytearray(10)` the invocation creates a bytearray object able to store ten bytes and fills the whole array with zeros.  
  
  - Characteristics:  
    - Bytearrays are mutable  
    - You can use the `len()` function on them  
    - You can access any of their elements using conventional indexing  
    - You can't set a byte array an element with a value that is not an integer (TypeError)  
    - You are only allowed to assign a value in the range 0 to 255 inclusive (or else you will get a ValueError)  
    - You can treat bytearray elements as integer values  
    - Refer to `28.bytearray.py`  

  - Writing a byte array to a binary file.  
    - `readinto()` is used to read the contents of the binary file into an existing bytearray.  
    - the `readinto()` method also returns the number of successfully read bytes.  
    - if the bytearray is smaller than the contents of the file, the operation will stop before the end of the file.  
    - when working with a binary file, you need to include `b` in either the `open()` or `close()` methods.  

  - Reading bytes from a stream.  
    - `read()` is also available to read a binary file.  
    - **Caution** if you try to invoke this without any arguments, it tries to **read all all the contents of the file into memory**.  
      Which could potentially crash the OS if the file is larger than the available memory.  
    - This methods works with the **bytes** class.  
      The **bytes** class has similar properties to the **bytearray** class, _with one major difference_... The bytes class is **immutable**.  
    - Refer to `30.bytes.py`  
    - You can specifiy an argument for `read()` which will read that many bytes.  
    - Refer to `31.bytes.py`  



<ins>Refer to the summary section</ins>  
https://edube.org/learn/pe-2/section-summary-107  


### Module 4.4  
#### The os module  

This module lets you interact with the OS.  
The os module provides functions that are available on linux or windows operating systems.  

In addition to file and directory operations, the os module enables you to:  
  - get information about the operating system  
  - manage processes  
  - operate on I/O streams using file descriptors.  

The `os` module contains a few different methods:  
  - `.uname()` This will return information on the current operating system, including the following attributes:  
    - **systemname** — stores the name of the operating system  
    - **nodename** — stores the machine name on the network  
    - **release** — stores the operating system release  
    - **version** — stores the operating system version  
    - **machine** — stores the hardware identifier, e.g., x86_64  
    - refer to `33.os.py` for an example.  
  - `.name` is a property that you can you to get one of the following values: **posix**, **nt** or **java**(if your code is written in Jython)  
  - `.mkdir()` this will create a directory, this function accepts a string. You can use a relative or absolute path.  
    The function can also take the `mode` argument  
  - `makedirs()` this will recursively create directories like the `mkdir -p` command on linux.  
  - `.listdir()` this will output the contents of the current directory or a directory that has been passed as a string.  
    This method omits the entries `.` and `..`  
  - `chdir()` this will change directories and obviously needs a string.  
  - `getcwd()` this will get the current working directory.  
  