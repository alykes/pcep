# Tests the assertion is correct, if it isn't, it will raise an AssertionError
import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

## Remeber that an exception will be raised if the evaluation of the assert is zero, and empty string or None
def foo(x):
    assert x        # This will raise an AssertionError as the assert will evaluate to Zero and will go directly into the except clause
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")   # Will jump to this branch here