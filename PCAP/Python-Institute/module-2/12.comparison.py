# Test examples here.
print('alpha' == 'alpha')
print('alpha' != 'Alpha')
print('alpha' < 'alphabet')
print('beta' > 'Beta')


print('10' == '010')    # False
print('10' > '010')     # True
print('10' > '8')       # False
print('20' < '8')       # True
print('20' < '80')      # True

print('10' == 10)       # False
print('10' != 10)       # True
print('10' == 1)        # False
print('10' != 1)        # True
print('10' > 10)        # TypeError

