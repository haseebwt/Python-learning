# If statements - Test:

# Task 1 - Create a dictionary named employees. Assing names to the 'key', and working hour to
# the key value

employees = {"Jack": 6, "Russel": 10, "Keren": 2}

print("(1) - Printing the dictionary 'employees': "+str(employees))

# Extra line

print("\n")

# Task 2 - Find an employee the in dictionary who works 5 - 8 hours. Check every employee

if employees["Jack"] >= 6 and employees["Jack"] <= 8:
    print("(2) - Jack fits for the job.")

elif employees["Russel"] >= 6 and employees["Russel"] <= 8:
    print("(2) - Rusel fits best for the job.")

elif employees["Keren"] >= 6 and employees["Keren"] <= 8:
    print("(2) - Karen fits the best for this job.")

else:
    print("(2) - There is no one who fits.")

# Extra line

print("\n")

# Task 3 (a) - Office is looking for an employee who will work 2 OR 4 hours

# Task 3 (b) - Manager wants to know what is the exact time she could spend at work

if employees["Jack"] == 2 or employees["Jack"] == 4:
    print("(3) - Jack fits for the job")

elif employees["Russel"] == 2 or employees["Russel"] == 4:
    print("(3) - Rusel fits best for the job.")

elif employees["Keren"] == 2 or employees["Keren"] == 4:
    print("(3) -  Karen fits well for this job")
    # Nested if statement
    if employees["Keren"] == 2:
        pass
    
    elif employees["Keren"] == 4:
        pass
    
    else:
        print("(3) - Silly.")
else:
    print("(3) - There is no one who fits.")

# -------------------------------------------------------------------------------------------- #