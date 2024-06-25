# Methods - Advnaced

# In Python, methods/functions can have arguements with key and value. 
# Just like we saw in Dictionaries.

# For example:

def mobile_brands(brand1,brand3,brand2):

    print(f"The 3rd brand is: {brand3}")



mobile_brands(brand1='Apple', brand2='Samsung', brand3='Google Pixel')


# Python can also have arbitrary arguemnts. What this means is that a method could have a random number of arguments.

# For example:

# Singe star ( * ) = Tuple collection

def clothing(*company):

    return company[1]

print(clothing('Adidas','Nike','Polo'))



# We can also have abritrary keyword arguments. They work just like keyword arguments but this time
# we don't have a definite amount of arguments.

# Double star ( ** ) = Dictionary collection

def brand(**company_info):

    print("The info is: "+str(company_info))


brand(Brand = 'Apple', Mobile = 'iPhone 11 Pro Max')