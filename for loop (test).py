# Loops - for loop TEST

# Task 1 - Make a list called Businesses
businesses = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10 ,15001]

print("(1) - Printing the collection: "+str(businesses))
 
total_tax = 0
#  Space
print('\n')

# Task 2 - Businesses with gross incomes in between 1 - 2k will pay 5% tax

print("(2) - Businesses with gross incomes between 1 - 2k pay: ")

for income in businesses:
    if income>=1 and income<=2000:
        tax = income * 0.05
        
        print("(2) - Total tax: $"+str(tax))
        net_income = income - tax
        print("(2) - Net income: $"+str(net_income))
        healthcare = net_income * .98
        print("(2) - Income after healthcare reduction: $"+str(healthcare))
        total_tax1 = total_tax + tax
        # print("(2) - Total tax: $"+str(total_tax))
        print("\n")

# Space
print('\n')

# Task 3 - Businesses with gross incomes in between 2k - 5k will pay 10%

print("(3) - Businesses with gross incomes in between 2k - 5k pay:") 

for income in businesses:
    if income>=2000 and income<=5000:
        tax = income * 0.1
        
        print("(3) - Total tax: $"+str(tax))
        net_income = income - tax
        print("(3) - Net income: $"+str(net_income))
        healthcare = net_income * .98
        print("(3) - Income after healtcare reduction: $"+str(healthcare))
        total_tax2 = total_tax + tax
        # print("(3) - Total tax: $"+str(total_tax))
        print("\n")
# Space
print('\n')

# Task 4 - Businesses with gross incomes in between 5k - 15k will pay 15% tax.

print("(4) - Businesses with gross incomes in between 5k - 15k will pay: ")

for income in businesses:
    if income>=5000 and income<=15000:
        tax = income * 0.15
        
        print("(4) - Total tax: $"+str(tax))
        net_income = income - tax
        print("(4) - Net income: $"+str(net_income))
        healthcare = net_income * .98
        print("(4) - Income after healtcare reduction: $"+str(healthcare))
        total_tax3 = total_tax + tax
        # print("(4) - Total tax: $"+str(total_tax))
        print("\n")

    
# Space
print('\n')

# Task 5 - Above 15k will pay 17% tax

print("(5) -  Businesses with gross incomes above 15k will pay: ")

for income in businesses:
    if income > 15000:
        tax = income * 0.17
        
        print("(5) - Total tax: $"+str(tax))
        net_income = income - tax
        print("(5) - Net income: $"+str(net_income))
        healthcare = net_income * .98
        print("(5) - Income after healtcare reduction: $"+str(healthcare))
        total_tax4 = total_tax + tax
        # print("(5) - Total tax: $"+str(total_tax))
        print("\n")
# Space
print('\n')

mo = total_tax1+total_tax2+total_tax3+total_tax4

print("(7) - Total tax collected from all the businesses: "+str(mo))