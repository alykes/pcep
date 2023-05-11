def outer_example(par_example):
    loc_example = par_example

var_example = 1
outer_example(var_example)

# print(par_example)    # These statments return errors because the par and loc variables only exist in the outer_example() function!
# print(loc_example)


# This is a basic example of how a closure works.  
def outer(par):
    loc = par

    def inner():            # the inner() function is only available while in outer(), no other part of the code can access it.
        return loc          # inner() can use any of the entities of outer as it is in scope.
    return inner            # The outer() function returns a copy of the inner() function, one that was FROZEN at the moment of outer()
                            # The frozen function retains its full environment including the state of all local variables. So the value
                            # of loc is successfully retained, although outer ceased to exist

var = 1
fun = outer(var)            # The function returned during the outer() invocation is a closure.
print(fun())


