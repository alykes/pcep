# A basic example of how to invoke a generator.  
def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)

