# While Loop - Advanced

# There is way to stop a while loop even when the condition is true.
# We can use 'break' to achieve it.

number = 0

while number < 10:

    if number >= 2:
        print(f'Number is: {number}')
        break


    print(f"The number is: {number}")

    number += 1

# Using 'else' in while loop:
cum = 0

while cum < 5:
    print( f"Load is: {cum}" )
    cum += 1

else:
    cum = cum * 100
    print(f"Load is now: {cum}")   