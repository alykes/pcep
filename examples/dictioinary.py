dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
print(v)    # two

for k in range(len(dictionary)):    # k => 0, 1, 2
    print('k:', k, 'v:', v)
    v = dictionary[v]               # three, one, two
    print('The lookup value is now:', v)

print['The final value of v is:', v]