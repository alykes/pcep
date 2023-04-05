def greet(text):            # Function named greet that takes one argument, a text value

    def print_greet():      # This function prints the text, this is a nested function. The nested function has access to the variables available in the outer function.
        print(text)         # This becomes a CLOSURE the moment it references a variable from the outer function (else it would simply be a nested function)

    return print_greet      # This returns the nested function without actually calling it, that's why the brackets are left out.


say_hello = greet('Hello')  # Because we return a value from the outer function, the value can be saved in a variable. This basically returns the closure from the outer function.
say_hello()                 # This line means try to invoke whatever is contained in the say_hello variable. The closure has a print statement so you can see the output.

# Free variables are those that are used by closures and don't get destroyed when they are first used. 