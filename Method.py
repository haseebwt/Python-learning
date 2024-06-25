# OOP | Method

# Method is a block of code that can be executed by calling it

# For example:

x=4

# Simple method/function (No data passed to it)

def my_method():
    print("Hellow from my 'my_method'!")

my_method()


# Simple methood/function (Data passed)

def my_age(age):
    print(f"My age is: {age}")

my_age(25)

def sum(x,y):
    z =  x + y
    print(f"Sum of your numbers is: {z}")



# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
# sum(x,y)

# ====================================================================================================================== #
print('\n')

def salary_calculation(salary):
    
    salary_of_employ = salary * 0.98
    print(f"The salary is: {salary_of_employ}")

salary_calculation(1000)

# OR

def salary_calculation2(salary,tax_reduction):

    salary_of_employee = salary * tax_reduction
    print(f"The Salary is: {salary_of_employee}")

salary_calculation2(200,.98)