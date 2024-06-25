# Methods - Practice:

def new_line():
    print('\n')

# PART A:

# Create a function called 'sorting()'

print(" - PART A - ")

def sorting(*languages):

    for i, language in enumerate(languages):

# i = index, language = value
# enumerate = [i, value] or [0, Python]

        if language == 'Java':
            print("The language is Java!")            
            print("Printing the letters in Java: ")

            for character in language:
                print(character)

        else:
            print("The language is not Java! It is: "+language)

        i += 1

sorting('Python', 'Java')
new_line()

sorting('Python', 'Java', 'GO!')
new_line()

sorting('Python', 'JS', 'C++')

new_line()

# PART B:

print(" - PART B - ")

def tax_calculation(gross_salary,tax=0.22):

    net_salary = gross_salary * (1 - tax)

    print("The net salary is: "+str(net_salary))

    return net_salary

new_line()

def tax_limitor(net_salary):

    if net_salary >= 5800:
        print(f"The net salary is above 5800. ({net_salary})")

    else:
        print(f"The net salary is below 5800. ({net_salary})")

net_salary1 = tax_calculation(5000,0.2)
tax_limitor(net_salary1)
new_line()

net_salary2 = tax_calculation(6000,0.22)
tax_limitor(net_salary2)
new_line()

net_salary3 = tax_calculation(10000)
tax_limitor(net_salary3)