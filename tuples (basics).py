# Tupels - Basic:-

# Create a tuple called 'professions_in_industry':
professions_in_industry = ('front-end','back-end','dev_ops','qa')

print("Respected professions in the industry: "+str(professions_in_industry))

# Find out the type of collection:

collection_type = type(professions_in_industry)
print("1st method: "+str(collection_type))

# or

print("2nd method: "+str(type(professions_in_industry)))

# Print cell number 1 in the tuple:
print("Printing the first cell: "+str(professions_in_industry[0]))

# Print the last cell of the collection:
print("Printing the last cell: "+str(professions_in_industry[-1]))

# Print a range of cells:
print("Printing a range of cells: "+str(professions_in_industry[0:3]))

# Print out the length of the tuple:
print("The length of the collection is: "+str(len(professions_in_industry)))