# For loop - Advanced

# range():
# To run a loop for a specific number of times we use 'range()'

# 1st Example:
for x in range(6):
    print(x)

# Space
print('\n')

# 2nd Example:
# We can tell the range function where to start and stop
for y in range(68 , 70):
    print(y)

# Space
print('\n')

# 3rd Example:
# We can also tell the range function what should it add to the iteration

for z in range(0,      10,       2):
            # start   stop    amount to add each time    
    print(z)

# --------------------------------------------------------------------------------------------- #

"""
Guidlines for bonus:

1) I want you to build a formula for bonuses.

2) Employees are placed in cells by their work ethics.

3) Give each employee a bonus which will be based on their place in the list, multiply the bonus by 100 
(bonus = place * 100)

4) Give bonus by jumping +3 each time in the list

5) First employee (cell index 0) does not deserve a bonus. 
"""
# Space
print('\n')

salary = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

for place in range(0, 11, 3):
    if place == 0:
        pass
    
    else:
        salary_with_bonus = salary[place]+ place * 1000
        print(salary_with_bonus)