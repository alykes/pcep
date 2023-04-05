## Miscellaneous Stuff  
The stuff that didn't fit into any other area but need to know for the exam.  

### List comprehension  
- Refer `lc.py`  
- There is a control variable, then a loop. eg `[num for num in range(1,101)]` where `num` is the control variable, and the segment that starts with `for` is the start of the loop. Also note the `[]`, which means a list.  


### Lambda  
lambda functions are used to simplify code, to make it easier to understand.  
Making it shorter and clearer.  
A traditional function looks like this:  
```
def function_name(param1, param2):
    # instruction 1
    # instruction 2
```  

A lambda function, looks like this:  
`lambda param1, param2: # instruction`  

- A lambda can be used without giving it a name.  
- The other **major** difference is that a lambda can only contain a **single instruction**.  
- Refer to `lambda-1.py` for an example.  
- Note three things:  
  - lambda does not need a return keyword.  
  - It is much shorter.  
  - It does not need a name.  
- To call a lambda that doesn't have a name, you store the lambda function into a variable.  
  `lambda_sum = lambda e, f: sum e + f`  
  `lambda_sum(2 + 3)`
- One of the benefits of a lambda function is that is can be passed around just like a variable. Refer to `lambda-2.py` and `lambda-3.py`  
- Lambda functions can be referred to as:  
  - Functions without names  
  - Anonymous functions  

#### map() and filter() with lambdas  
- Two functions that take lambdas as an argument are `map()` and `filter()`  
- `map()` will create a list from a lambda function.  
- `filter()` will only keep the elements that match the filter in the lambda function.  
- Refer to the examples `fliter.py` and `map.py`  

#### Closures  
- A closure is a technique for implementing lexically scoped name binding in a language with first-class functions.  # Eeeeek!!! or....  
- A closure is a function defined inside another function that remembers the values of the outer function.  
- Basically a function within a function  
- Refer to `closure-1.py` and `closure-2.py`  
- Closures can replace small classes, eg, those that have one custom method.  

### File Handling  
- Persistence of data  
- Linux and windows use different rules for file paths, specifically `\` vs `/`  
- Python uses intermediate entities to work with files, they are typically called `handles` or `streams`  
- When you want to work with a file, you need to open a `stream` to the file (open a file).  
  - Python creates an object depending on how you open the file.  
- Once you finish working with the file, you should always disconnect the stream (close a file).  
  - Python will destroy the object once you close the file and have finished working with it.  
- Streams have a heirarchy, at the top is `IOBase` and below that are the following `RawIOBase` `BufferedIOBase` and `TextIOBase`  
- Two categories, text and binary files and therefore two streams `text streams` and `binary streams`  
- Line endings:  
  - Linux `\n`  
  - Windows `\r\n`  
- Text files are read line by line.  
- Binary files are read as sequences of bytes. Examples include images, audio files, video clips, executable files etc (single bytes or bigger blocks of bytes)  

#### Text files - Reading  
- Always use a `try: except:` block for working with files.  
- open a file as follows, `stream = open('FILENAME')`, you assign it to a variable so that you can work with the file handler/stream.  
- Always ensure that you close every stream once you have finished working with it or else you can run into memory issues.  
- Refer to `file-1.py` for some examples.  
- `read()` - This method is the simplest for reading content of a file from a file. returns the whole content.  
  - `read(10)` - You can specify how many bytes (typically one byte = character) that you would like to read.  
    - The stream moves inside the file and will allow you to read the next 10 bytes.  
  - When the stream reaches the end of the file, _an empty string is returned._ No error is shown!  
- There are advantages of reading a file character by character.  
  - It allows you to analyse the contents of the file. eg, how many digits, how many spaces etc.  
  - It allows you to protect the file system, eg, reading a 1 TB file all at once, will probably make the program crash!   
- `readline()` - Allows you to read the file, line by line and finally returns an empty string if it hits the end.  
- `readlines()` - Returns a list of strings, one string per file line. By default will read the entire file.
  - You can specify the amount of bytes to read per line. 
    - `readlines(2)` - If a file contains a single character per line, say `a` and `b` on separate lines, `readlines(2)` would return `['a', 'b']`  
    - `readlines(2)` - If a file contained two letters on each line, say `aa` then `bb` then `cc`. The result would be `['aa']`  
    - `readlines(2)` - If the amount of bytes specified does not capture one single line, then the buffer will be autoincreased to capture at least one line!  
    - An empty list means that you have reached the end of the file.  
- A file stream is an iterable object, refer to files-9.py  

#### Text files - Writing  
- If you create a stream to a writable file, each time you run the code, the file will be re-created from scratch!  
- If you use 'w' on an existing file Python will delete the content and write what ever you provide to it.  

#### Binary files
- Text and binary are just simply files or containers for data. They are squences of bytes.  
- Bytes are always organised in a certain way.  
- Python File Handling:  
  - Binary files  
    - raw data  
    - hard to read  
    - can store anything  
    - only chosen if text files not possible  
  - Text files  
    - text data  
    - easy to read  
    - can store a lot of useful information  
    - preferred choice (if possible)  
- Will only provide the basics for the PCAP exam.  
- Byte Array, an array of bytes and is conceptually similar to a list. It has containers for bytes.  
  - `data = bytearray(100)` will create an array with 100 bytes and each one is set to 0  
  - `data[0] = 100` will store the first byte of the bytearray to the binary representation of 100, NOTE, you can only set bytes that are between 0 and 255 inclusive  
- To write to a binary file, you use the argument `'wb'` to _write_ to _binary_ file.  
- To read a binary file, you use the argument `'rb'` to _read_ the _binary_ file.  
- `read(10)` - This reads the first 10 bytes into memory. This method also creates a special class called **bytes**, which is immutable! (**NOTE** it is different to the **byte_array** class)  
  - You can wrap the `bf.read()` method to as follows `bytearray(bf.read())` to get a _byte_array_ rather than a _bytes_ object.  
  - The other option is to create it manually eg `data = bytearray(10)`  

#### File Handling modes  
- There are a bunch of different arguments that you can use.  
  `open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`    
- Refer to the table below for available modes.  
|---|---|
|Character|Meaning|
|'r'|open for reading (default)|
|'w'|open for writing, truncating the file first|
|'x'|open for exclusive creation, failing if the file already exists|
|'a'|open for writing, appending to the end of the file if it exists|
|'b'|binary mode|
|'t'|text mode|
|'+'|open for updating (reading and writing)|  

- The modes can be combined to form some more complex file streams, like 'w+', writing as well as reading and updating. etc

#### Predefined streams  
- There are three defined streams that don't need any further preparation.  
- You don't need to call the open function.  
  - `sys.stdin` - this stream is used for direct input (from the console)  
  - `sys.stdout` - `sys.stdout.write('Will only print strings')`, to print an integer, you would have to cast it with `str(3)`  
  - `sys.err` - Standard error, it's a semantic description. Use the standard error stream for errors, just know it exists for the exam.    

#### Stream Errors  
- Not exist, don't have the proper permissions etc...  
- All file operation errors refer to specific file errors, eg `[Errno 2]` if the file doesn't exist.  
  - to access this number, you can do so with `print(e.errno)` <-- where this is in the except block. Refer to `streams-error.py`  
  - to grab the description for the error number, you can do the following: `print(strerror(e.errno))` in the except block but you need to add `from os import strerror` for this to work!  
- Good to use if you want to react differently to various problems.  

