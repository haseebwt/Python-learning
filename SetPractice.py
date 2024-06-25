# Sets (Practice) :

# Task - 1: Create a set with the following values:
# cola, sprite, beer, water, soda

drinks= {'Cola', 'Sprite', 'Beer', 'Water', 'Soda'}

print("(1) - Printing the set 'dirnks' :"+str(drinks))

# Task - 2: Add an additional value 'soda'
# Question: Will Python print it twice?

drinks.add('Soda')

print("(2) - Add a new value 'Soda' to the Set: "+str(drinks))
print("Answer: Because it was a duplicated, Python only printed it once.")

# Task - 3: Delete the 'soda' value:

drinks.remove('Soda')

print("(3) - Removed the value 'soda': "+str(drinks))

# Task - 4: Make a copy of the set:
drinks2 = drinks.copy()
print("(4) - Printing the newly coppied Set: "+str(drinks2))

# Task - 5 (Bonus): Print the length of set:

print("(5) - Printing the length of the set 'Drinks' :"+str(len(drinks)))

# ------------------------------------------------------------------------------------- #