## Shows the subclsses of the BaseException class
for subclass in BaseException.__subclasses__():
    print(subclass.__name__)


## Shows the subclsses of the Exception class
for subclass in Exception.__subclasses__():
    print(subclass.__name__)