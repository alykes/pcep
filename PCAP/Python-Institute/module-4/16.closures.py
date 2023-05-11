# An example of how to create multiple closures from one piece of code.
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

# Result:
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64