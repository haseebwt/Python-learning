#Python Based Calculator By Haseeb T-T

def add(num1 , num2):
    return num1 + num2

def substract(num1 , num2):
    return num1 - num2

def multiply(num1 , num2):
    return num1 * num2

def devide(num1 , num2):
    return num1 / num2

print("Select The Operation - \n"
        "1 . Add\n" \
        "2 . Substract\n" \
        "3 . Multiply\n" \
        "4 . Devide")

Select = int(input("Select Operation 1/2/3/4 : "))

number_1 = int(input("Select First Numebr : "))
number_2 = int(input("Select Second Number : "))

if Select == 1:
    print(number_1, "+", number_2, "=",
                        add(number_1 , number_2))
elif Select == 2:
    print(number_1, "-", number_2, "=", 
                        substract(number_1 , number_2))
elif Select == 3:
    print(number_1, "X", number_2, "=",
                        multiply(number_1 , number_2))
elif Select == 4:
    print(number_1, "/", number_2, "=",
                        devide(number_1 , number_2))

else:
    print("Invalid Input.")

