print(len([i for i in range(0, -2)]))
# range tries to make a series of numbers from 0 to -2 going up, so never reaches -2
# you need step -1 

t = (1, )
t = t[0] + t[0]
print(t)
# Evaluates to 2