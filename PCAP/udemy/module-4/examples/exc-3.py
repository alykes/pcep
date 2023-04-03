def return_bigger(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError
    if b > a:
        return b
    else:
        return a


print(return_bigger(10, 50))




def return_inverse(x):
    try:
        return 1/x
    except:
        print('Something went wrong!')
        raise   # This handles the exception partially.

return_inverse(10)
