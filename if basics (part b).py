# If Statement - Basics (Part: B)

# Logical Operators: 
# There are two types of logical oprators that are used in if statement. First one is 'and' and
# second is 'or'.

# We can have two conditions in one if statement. "And" means that we want both the conditions
# in the if statement to be true. "Or" means we want only one condition in the if statement
# to be true.

# For example:

x = 2
y = 9
# And
if x == 2 and y == 0:
    print("X is "+str(x)+". Y is "+str(y)+".")
else:
    print("You got it wrong, cheef.")

# Or
if x == 9 or y == 2:
    print("Yup!")
else:
    print("Neither of the conditions were true!")

# --------------------------------------------------------------------------------------------- #

# Nested if statements:

# In ‘if’ statements we can nest them one in the other.
# Meaning if some ‘if’ statement came up ‘True’, then go inside another ‘if’ statement which can
# also be ‘True’ or ‘False’.

# For example:

age_2 = 30
gender = 'Female'

if age_2>20:
    if gender == 'Male':
        print("Your age is 20 and you are a male!")
    else:
        print("Not a man! Boooo Women aren't real.\n")
else:
    print("YOU ARE NOT ABOVE 20!! Kiddo!\n")

# --------------------------------------------------------------------------------------------- #

age = 30
name = 'James'

# Example: 1 - Logical Operator 'and'
if age > 20 and name == "James":
    print("Example: 1 - My name is James and I am over 20.")
else:
    print("Example: 1 - Default exit point.")

# Example: 2 - Logical Operator 'or'
if age > 20 or name == "James":
    print("Example: 2 - My name is James and I am over 20.")
else:
    print("Example: 2 - Default exit point.")

print("\n")

# Nested If statement:

married = True

if age > 20 and name == "James":
    if married == True:
        print("Example: 3 - Good luck! It's gonna be a long (happy) ride :)")
    else:
        print("Example: 3 - Nested 'else'")
else:
    print("Example: 3 - Parent 'else'")

# --------------------------------------------------------------------------------------------- #