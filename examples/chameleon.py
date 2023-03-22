dictionary = {}
my_list = ['a', 'b', 'c', 'd']

for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], ) # Assigns the key referenced with a tuple value 
    # {'a': ('a',), 'b': ('b',), 'c': ('c',)}

print('***')
print(my_list)      # ['a', 'b', 'c', 'd']
print(dictionary)   # {'a': ('a',), 'b': ('b',), 'c': ('c',)}
print('***')

for i in sorted(dictionary.keys()): # sorted removes dict_keys and simply returns ['a', 'b', 'c']
    k = dictionary[i]   
    print(k)        # ('a',) ('b',) ('c',) 
    print(k[0])     # a b c