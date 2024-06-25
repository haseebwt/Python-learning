# Tuples - Practice (Test) :

# Task - 1: Create a tuple collection called "techonological_terms"

technological_terms = ('Python', 'VS Code', 'Tuple', 'Collection', 'String')
print("(1) - Printing tuple 'techonological_terms' : "+str(technological_terms))

# Task - 2: Print the following sentence using cell extraction:
# "We are ninja developers. We write python code in VS Code, and now practicing tuple collection
# topic, that contains string vairables"

# a) Usual extraction method
# b) Negatice extraction method

print("\n(2) - We are Ninja Developers. We write "+technological_terms[0]+" code in "+
      technological_terms[-4]+", and now practicing "+technological_terms[2]+" "+
      technological_terms[-2]+" topic, that contains "+technological_terms[4]+" variables.")

# Task - 3: Insert values 'float' and 'list' at the end of the tuple
tech_terms_list = list(technological_terms)

tech_terms_list.append('float')
tech_terms_list.append('list')

technological_terms = tuple(tech_terms_list)

print("\n(3) - Collection after adding 'float' and 'list' : "+str(technological_terms))
print("What type of collection is the above collection ?"+str(type(technological_terms)))

# Task - 4: Create a single cell tuple with the number '1' in it and also print out the type

single_cell = (1,)
print("\n(4) - Tuple with only one singular value: "+str(single_cell))
print("What is the type of above collection ?"+str(type(single_cell)))

# ---------------------------------------------------------------------------------------------- #