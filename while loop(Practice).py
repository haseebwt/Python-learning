# PART 1

# Create a list of 'ages'

print("- PART A -")

ages = [5, 6, 24, 32, 21, 70]

ages.sort()

counter = 0

# Print all the ages under the 30 

while ages[counter] < 30:

    print(f"The age is: {ages[counter]}")

    counter += 1

print("\nAll of the ages below 30 ^ ")
print("The value that caused the loop to stop: "+str(ages[counter]))

print("\n")


# PART B    

# If value is bigger than 20, break the while loop

print("- PART B -")

count = 0

while ages[count] < 100:
    
    if ages[count] > 20:
        print("The loop broke because the age is more than 20: "+str(ages[count]))
        break

    print(f"The age is: {ages[count]}")
    
    count += 1 

print('\n')

# PART C

print("- PART C -")

num = 0

while ages[num] < 70:
    
    ages2 = ages[num] + 2
   
    print(f'\nThe age is: {ages[num]}')

    print(f"The new number is: {ages2}")
    
    num += 1

else:
    print("\nI'm inside 'else' because of: "+str(ages[num]))