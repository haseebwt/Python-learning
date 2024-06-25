# Nested Dictionary:

# Definition:
#           A key containing one or more values contained within a single dictionary is called Nested Dictionary
# For example: dictionary = { parent_cell1: {"key":'value', "key":'value'} }

# A nested dictionary:

daniel = { "Age":40, "Children":{"Asher":'boy',"Selina":'girl'} }

# Extract a value:

daniel["Children"]

print(daniel["Children"])

# Extract value in a nested dictionary:

daniel["Children"]["Asher"]

print(daniel["Children"]["Asher"])

# Duplicate dictionary:
# We can duplicate dictionary by making a new dictionary and using the '.copy()' to copy a dictionary into it:

more_daniel = daniel.copy()

print("Printing the dictionary: more_daniel : "+str(more_daniel))

# Add a new cell. We can add a new cell by mentioning the dictionary and putting the new key in square brakckets and assign it a value:

daniel["Wife"]=True

print("Printing the Daniel dictionary after adding a new cell using comamnd : "+str(daniel))

# Empty out a dictionary:
# We can empty out a dictionary by using the action '.clear()':

daniel.clear()

print(daniel)