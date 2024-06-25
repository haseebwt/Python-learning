# Sets :

# Sets are very different from Lists. Though they might look like lists but they aren't
# Sets can be donated by curly brackets '{}' and Lists are denoted by square brackets '[]'
# Sets can't have duplicates or reoccuring data whereas Lists allow such a thing
# Sets don't have indexes either. They function like a Dictionary.


# Example of a set:

set1 = {'banana','apple','pp'}

print(set1)

# Extract values in Sets:
# Since sets don't have indexes we can't really ask Python to print a specific value. Instead,
# we would ask python if the cell already exists or not by using Boolean.

# For example:
print("Is Banana an existing cell value in the set ? "+str( 'banana' in set1))

print("Is Haseeb an existing cell value in the set ? "+str('haseeb' in set1))

# Delete an item from a Set:
# We can use the '.remove()' action to perform it:

set1.remove('apple')
print(set1)

# Add an item to a Set:
# We can use the '.add()' action to perform this:

set1.add('shrimp')
print(set1)

# If we have duplicates, Python will just ignore them and print the value once.
# For example:

set2 = {'shrimp','apple','shrimp','sushi','shrimp'}
print(set2)