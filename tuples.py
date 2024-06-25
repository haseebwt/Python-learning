# Tuples :- 

# It is similar to 'list' and 'sets' but not entirely same.
# You can't change the values inside the tuples. Once you've made a collection, it's always going
# to stay there.

# Example of tuples and how to manipulate it:

professions = ("back-end","front-end","dev_ops")
#Index             0    ,      1    ,    2     

# Accessing cells in tuples:
# First method:
print("I like the profession "+str(professions[2]))

# Second method:
print("I hate being a "+professions[-3]+" developer.")

# Acces a range of cells:
print(professions[0:3])

# ---------------------------------------------------------------------------------------------- #