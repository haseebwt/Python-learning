# EH - Practice:

# Task 1:-

try:
    x = 5
    print("The number is: "+ x)

except:
    print('"The number is: "+ x: '"We didn't convert the variable into string!")

    print('Correction: "The number is "+ str(x)')
    print("The number is: "+str(x))

# Task 2:-
print("\n")

try:
    y + 5

except:
    print("'y + 5': This didn't work because y was not defined!")

    y =+ 5

    print("Correction: 'y =+ 5'")
    print(f"Value of 'y': {y}")

# Task 3:-
print('\n')

try:
    list = [1, 2, 3, 4]
    print(list[6])

except:
    print("'print(list[6])' : This doesn't work because the list only contains 3 indexes!")

    print("Correction: 'print(list[3])'")
    print(f"The element of index '3': {list[3]}")