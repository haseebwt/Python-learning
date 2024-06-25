# Collections - Dictionary (basics)

# Creat a new Dictionary
new_employee = {'first_name' : 'David', 'salary' : 10000, 'company' : 'google'}

# Print the Dictionary
print("Printing the Dictionary : "+ str(new_employee))

# Get cell value - (First way)
print("Get value of 'first_name' key : "+str(new_employee['first_name']))

# Get cell value - (Second Way)
print("Get value of 'salary' key : "+str(new_employee.get('salary')))

# Remove dictionary cell by using ".pop()"
new_employee.pop('salary')
print("Remove dictionary cell by using '.pop()' : "+str(new_employee))

# Show Dictrionary 'keys' by using ".keys()"
print("Get all 'keys' out of the dictionary : "+str(new_employee.keys()))

# Show Dictionary 'values' by using ".values()"
print("Get all 'values' out of the  dictionary : "+str(new_employee.values()))

# Use a variable and place it inside a dictionary cell
job_title = 'developer'
new_dictionary= {'job_title' : job_title}
print("Print the 'new_dictionary' : "+str(new_dictionary))