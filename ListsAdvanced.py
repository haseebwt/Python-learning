# First create a simple list:

numbers_list = [1,34,6968,42.0]

# Find out the Length of a List. Now length of a list and index of a list are two different things
# length defines the number of elements present in the list. Whereas index defines the number of cells
# which always starts from 0. The elements are placed inside the cells.

# Print the lenght of the list:

print("The length of the list is : "+str(len(numbers_list)))

# Change the value of a cell:
print("The list before the value change : "+str(numbers_list))

numbers_list[1]=35

print("The list after the value change : "+str(numbers_list))

# To add a new value at the end of an existing list. We use the action 'append(new_value)'

numbers_list.append(96)

print("The list after adding a new value : "+str(numbers_list))

# To add a new value in an existing cell. We use the 'insert(cell,new_value)' action.

numbers_list.insert(0,144)

print("The list after adding a new value to the cell 0 : "+str(numbers_list))

# To remove a value form a list. We use the action 'remove(value)'

numbers_list.remove(144)

print("The list after removing the value '144' : "+str(numbers_list))

# To remove an item from the cell index. We use the action 'pop(cell)' using only 'pop()' will
# remove the last value of the list. So 'pop()' works like 'append()'

numbers_list.pop(0)

print("The list after removing the cell '0' : "+str(numbers_list))

#----------------------------------------------------------------------------------------------#