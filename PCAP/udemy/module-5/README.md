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





