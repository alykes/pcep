# Test with different variable definitions to see what the outputs are
# NOTE you can have a CLASS variable and an instance variable with the same name and they act independently~
class ExampleClass:
    varia = 1
    def __init__(self, val):
        varia = val                 # This is a local variable only available inside this method (function)
        blaria = val                # This is a local variable only available inside this method (function), print(example_object.blaria) will not work
        # varia = 10                # To proves that varia and self.varia are not the same variable
        self.varia = val            # This is setting it to the instance variable or object variable
        ExampleClass.varia = val    # This sets the class variable


print(ExampleClass.__dict__)       

example_object = ExampleClass(2)

print(ExampleClass.__dict__)       

print(example_object.__dict__)     
print(example_object.varia)        # This will print 2, even if varia is assigned 10 because this is the object variable named varia! (not the local variable named varia)