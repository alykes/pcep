class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g(self):
        return self.f()

a = A()
print(a.g())