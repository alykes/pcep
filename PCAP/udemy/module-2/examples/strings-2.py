print(' '.join(['This is', 'a weird way', 'to join strings'])) # This says to join a space (the seperator) to each element
print('-'.join(['This is', 'a weird way', 'to join strings']))
print('\n'.join(['This is', 'a weird way', 'to join strings']))
joined_string = '\n'.join(['This is', 'a weird way', 'to join strings'])
print(joined_string)    # Works no problemo

print('How\tmany\t strings,\nDo you think   you will see? '.split()) # removes any additional whitespaces and considers \n and \t as delimiters as well.
split_string = 'How\tmany\t strings,\nDo you think   you will see? '.split()
print(split_string)    # Works no problemo

names = ['Ango', 'Betty', 'Greg', 'Arthur', 'Wayne', 'Cyndi']
sorted_names = sorted(names)    # Does not sort the original list in-place
print(names)        # Remains unsorted
print(sorted_names) # prints the sorted names list

other_names = ['Bongo', 'Ango', 'Lamango', 'Fonzo', 'Pachino']
other_names.sort()     # Sorts the original list in-place
print(other_names)     # Returns the sorted list

other_names_2 = other_names.sort()  
print(other_names_2)    # DOES NOT WORK, returns NONE!! Be aware of this.