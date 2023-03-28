# Similar to lists, elements can have same or different data types
# defined with () brackets

empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
three_el_tuple = 1, 2, 3, # The final comma after the number 3 is optional

print(three_el_tuple)

# mutable - freely updated any time you like, like a list
# immutable - doesn't change, stays the same, like a tuple or a string

user_data = ('Chad', 'American', 1969)
user_data = ('Katia', 'Russian', 1972)

# You cannot append an object to a tuple
# You cannot delete an object in a tuple

print(user_data[0]) # works fine

user_data[0] = 'Mark' # This doesn't work on a tuple!!!

