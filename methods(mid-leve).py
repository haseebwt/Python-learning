# Methods - Mid-Level:

def new_line():
    print('\n')


# In Python, functions/methods can have 'default value(s)' in their parameter(s).
# In case of no user input, Python will run the default value.

# Example:

def my_country(country = 'Canada'):
    print("My country is: "+str(country))

print(" (A) - Execution with user input:")
my_country('Italy')

new_line()

print(f" (B) - Execution without user input:")
my_country()

# We can use 'return' keyword to assign the answer to the function and assign that function to a variable

# Example:
new_line()

def multiply(x):
    return 5 * x

product = multiply(3)
print(product)