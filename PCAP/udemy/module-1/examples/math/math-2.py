import math

x = 3.6

print(math.ceil(x))     # result: 4  ==> rounds up to the nearest whole number
print(math.floor(x))    # result: 3  ==> rounds down to the nearest whole number
print(math.trunc(x))    # result: 3  ==> 


# ceil() examples
# goes to the highest number that is not less than the number itself
print(math.ceil(3.1))   # result: 4
print(math.ceil(3.505)) # result: 4
print(math.ceil(3.993)) # result: 4
print(math.ceil(3.0))   # result: 3 ==> because this is already a whole number

# ceil() with negative numbers
print(math.ceil(-10.1))     # result: -10
print(math.ceil(-1.505))    # result: -1
print(math.ceil(-0.993))    # result: 0

# floor() is the opposite of ceil and goes to the smaller whole number
print(math.floor(3.1))   # result: 3
print(math.floor(3.505)) # result: 3
print(math.floor(3.993)) # result: 3
print(math.floor(3.0))   # result: 3 ==> because this is already a whole number

# floor() with negative numbers
print(math.floor(-10.1))     # result: -11
print(math.floor(-1.505))    # result: -2
print(math.floor(-0.993))    # result: -1

# trunc removes the decimal part of the number and just returns the integer
print(math.trunc(3.1))   # result: 3
print(math.trunc(3.505)) # result: 3
print(math.trunc(3.993)) # result: 3
print(math.trunc(3.0))   # result: 3 ==> because this is already a whole number

# trunc() with negative numbers
print(math.trunc(-10.1))     # result: -10
print(math.trunc(-1.505))    # result: -1
print(math.trunc(-0.993))    # result: 0

# Other functions that also need to be known
# factorial()
print(math.factorial(3)) # 6 ==> 3 * 2 * 1
print(math.factorial(4)) # 24 ==> 4 * 3 * 2 * 1

# sqrt()
print(math.sqrt(16))    # 4.0 ==> take note that it returns a float
print(math.sqrt(9))     # 3.0 ==> take note that it returns a float

# hypot() # hypotenuse function
print(math.hypot(3, 4)) #result: 5.0 ==> where 3 and 4 are the two sides of a right-angled triangle. This also returns a float!