# Exception handling:

# We can tell python what to do if it encounters an erorr.
# For example::

try:
    if age > 20:
        print("The age is above 20!")

except:
    print("Age was not defined!")

    age = 3

    print('Age is now 3')

print('\n')

q = input("Enter a 6 digit code: ") 

if q.isnumeric():
    try:
        if len(q) == 6:
            print('Perfect!')

    except:
        print("Pincode must be 6 digits long!")