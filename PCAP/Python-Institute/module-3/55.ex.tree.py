# Prints out all the classes in teh BaseException Tree
def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)

    for subclass in thisclass.__subclasses__():
        print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)

# print_exception_tree() function takes two arguments:
#     a point inside the tree from which we start traversing the tree;
#     a nesting level (we'll use it to build a simplified drawing of the tree's branches)

