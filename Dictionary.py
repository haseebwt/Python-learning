# Quick Example
dictionary_example={'name': "Rachel", 'test_grade' : 98 }

# Pull out a 'value' of a cell - Way Number 1
# to pull out cell's 'value' we need to mention the 'key', like this
print("(1) - Pull out a value by mentioning the 'key' (Method 1) : "+str(dictionary_example['name']))

# Output : Rachel

#---------------------------------------------------------------------------------#

# Pull out a 'value' of a cell - Way Number 2
# We can also use the '.get()' action keyword, like this
print("(2) - Pulling out a value using '.get()' (Method 2) : "+str(dictionary_example.get('name')))

#Output : Rachel