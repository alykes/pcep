## Python Notes for PCEP

Best practise is to always use single quotes and escape characters if need be.  

can't start variables with a number  

can't use these variable names  
from  
global  

program is set of instructions executed by a computer  
instruction list is a set of instructions the given computer can execute  

Translation processes source code to machine code

*compilation* - compile once and anyone can execute  
*interpretation* - interpret source code every time you run programs, everyone need the interpreter to run  

top to bottom execution of the code  
throws errors based on the following:  
- lexis - using keywords as variables  
- syntax - forgetting brackets  
- semantics- multiple arguments for a command that doesn't accept them  

Always use 4 spaces for the indentation as a best practise

## Exceptions

`ZeroDivisionError`: raised by a division in which the divider is zero or is indistinguishable from zero (/, //, and %)  
`ValueError`: raised by the use of values that are inappropriate in the current context, for example, when a function receives an argument of a proper type, but its value is unacceptable, for example, int('')  
`TypeError`: raised by attempts to apply data of a type which cannot be accepted in the current context, for example, int(None)  
`AttributeError`: raised – among other occasions – when the code tries to activate a method that doesn't exist in a certain item, for example, the_list.apend() (note the typo!)  
`SyntaxError`: raised when the control reaches a line of code that violates Python's grammar, and which has remained undetected until now;  
`NameError`: raised when the code attempts to make use of a non-existent (not previously defined) item, for example, a variable or a function.  