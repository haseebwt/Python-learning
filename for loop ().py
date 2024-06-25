# Loops - for loop TEST

# Task 1 - Make a list called Businesses
businesses = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10 ,15001]

print("(1) - Printing the collection: "+str(businesses))
 
total_taxes = 0
#  Space
print('\n')

# Task 2 - blah blah

for single_income in businesses:

#  1k to 2k 
    if single_income>=1 and single_income<=2000:
        
        tax = single_income * .05
        
# 2k to 5k
    elif single_income>=2001 and single_income<=5000:

        tax = single_income * .1

# 5k to 15k
    elif single_income>=5001 and single_income<=15000:

        tax = single_income * .15

# 15k+
    else:
        tax = single_income * .17

    net_income = single_income - tax

    healthcare = net_income * .98

    print("\nPrinting income after health care reduction: $"+str(healthcare))

    total_taxes = total_taxes + tax

print("Print total of taxes: "+str(total_taxes))