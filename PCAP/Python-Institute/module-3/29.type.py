class Classy:
    pass


print(Classy.__name__)      # Classy
obj = Classy()
print(type(obj).__name__)   # Classy

# Added these here for testing
print(Classy)               # <class '__main__.Classy'>
print(obj)                  # <__main__.Classy object at 0x7f29ea8251d0> - I believe this can be overridden with _str
print(type(obj))            # <class '__main__.Classy'>

# print(obj.__name__)       # This will cause an AttributeError, as the object doesn't have a __name__ property
print(Classy._obj__name__)