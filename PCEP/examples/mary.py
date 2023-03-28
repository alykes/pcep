list_1 = ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(listing):
    del listing[3]
    listing[3] = 'ram'


print(my_list(list_1))
print(list_1)