name_original = 'Jon Snow'
name_new = name_original
name_original = 'Allanon'
print(name_original, name_new)


# The list_new is just a pointer to the orignal list
list_original = [1, 2, 3]
list_new = list_original # Just writes the pointer location to the new variable, they both reference the same list
list_original[0] = -5
print('Original List:', list_original, '\nNew List:', list_new)


# To copy a list, you use a slice
list_original = [1, 2, 3]
list_new = list_original[:] # This will then actively write each element to the new list
list_original[0] = -5
print('Original List:', list_original, '\nNew List:', list_new)


