# Tuples - (Advanced):-

# A quick example of Tuples:

clothes = ('pants', 'shirt', 'hat', 'socks')

# Changing/Adding/Removing value of tuples(technically)
# First, we have to make a list and assign our tuples collection to it and then change/add/remove
# the value in that list. After the changes have been made, we can assign the list back to a
# tuples collection.
# For example:

clothes_list = list(clothes)


clothes_list.append('underwear')

print("Printing the list converted from tuple: "+str(clothes_list))
print("VERIFICATION:\nIs the collection above a list or tuple ? "+str(type(clothes_list)))

clothes = tuple(clothes_list)

print("\nCollection after adding a value using the 'list trick': "+str(clothes))
print("VERIFICATION:\nIs the collection above a list or tuple ? "+str(type(clothes)))

# If we want to make a tuple with only one cell (for whatever reasons). It won't work like a 
# tuple. Instead, Python will recognise it as a string.
# For example:

tuple = ('penis')
print(type(tuple))
# output -> str

# To make a one cell tuple, we must add a coma after our value.
# For example:

real_tuple = ('penis',)
print(type(real_tuple))
# output -> tuple

# ---------------------------------------------------------------------------------------------- #