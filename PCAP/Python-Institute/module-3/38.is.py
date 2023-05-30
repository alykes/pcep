# Some good examples on how is works on objects stored in memory

class SampleClass:
    def __init__(self, val):
        self.val = val


object_1 = SampleClass(0)
object_2 = SampleClass(2)
object_3 = object_1             # This copies the reference for object_1 to object_3, essentially, they point to the same object now. 
object_3.val += 1               # Performing an operation on object_3 also affects object_1 as they are the same object!

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)
print(object_1.val, object_2.val, object_3.val)

string_1 = "Mary had a little "
string_2 = "Mary had a little lamb"
string_1 += "lamb"

print(string_1 == string_2, string_1 is string_2)

# Results: 
# False
# False
# True
# 1 2 1
# True False

# The results prove that object_1 and object_3 are actually the same objects, while string_1 and string_2 aren't, despite their contents being the same.