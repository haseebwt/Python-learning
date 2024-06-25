# For loop - Basics

# Using an if statement (with collections) in For Loop

fruits = ['banana', 'strawyberry', 'apple', 'orange', 'cherry', 'watermelon', 'orange']

# The loop will check each cell and print out orange. But it won't stop there. Instead, it will
# it will keep running until the list ends. Checking each and every cell.
print("The first for loop:")

for fruit in fruits:
    if fruit == 'orange':
        print(fruit)

# Using the function 'break', we can make the for loop stop as soon as it finds the first cell
# that matches the requirement.
print("\nThe second for loop: ")

for fruit2 in fruits:
    if fruit2 == 'orange':
        print(fruit2)
        break

# Using an if statement (with string) in For Loop
print('\n')
mango = 'cherry'

for check in mango:
    if check == 'r':
        print(check)

print('\n')
for check in mango:
    if check == 'r':
        print(check)
        break

# --------------------------------------------------------------------------------------------- #