# string_var is defined in the function
def show_truth():
    string_var = 'I feel a little stringy...' 
    print(string_var)

show_truth()


# string_var is defined outside of the function but still works!
def show_truth():
    print(string_var)

string_var = 'I feel a little stringy...' 
show_truth()

# variables have a scope outside of the function as well as inside

def show_truth():
    string_var = 'hehe, I\'m inside the function now!' # local var shadows the global variable
    print(string_var)

string_var = 'Defined outside the function!' # global var
print(string_var)
show_truth()
print(string_var)

# Result
# Defined outside the function!
# hehe, I'm inside the function now!
# Defined outside the function!
# The string is temporarily overidden in the function, this is called SHADOWING

# To change the value of the global var inside a function, use the keyword global
def show_truth():
    global string_var # this means, don't use shadowing, don't use a local variable (avoid it in the real world)
    string_var = 'hehe, I was defined in the function.' # local var shadows the global variable
    print(string_var)

string_var = 'Defined outside the function!' # global var
print(string_var)
show_truth()
print(string_var)
# Result
# Defined outside the function!
# hehe, I was defined in the function.
# hehe, I was defined in the function.


# Scopes and lists (and dictionaries) (but not tuples as they are immutable)!
# This shadows the global variable, so the list remains unchanged!
def show_truth():
    mysterious_var = ['Function Surprise'] # local var shadows the global variable
    print(mysterious_var)

mysterious_var = ['Surprise']
print(mysterious_var)
show_truth()
print(mysterious_var)
# Result
# ['Surprise']
# ['Function Surprise']
# ['Surprise']

# when using a method on a list in a function, the list will change
def show_truth():
    mysterious_var.append = ('Function Surprise') # local var shadows the global variable
    print(mysterious_var)

mysterious_var = ['Surprise']
print(mysterious_var)
show_truth()
print(mysterious_var)
# Result
# ['Surprise']
# ['Surprise', 'Function Surprise']
# ['Surprise', 'Function Surprise']