# OOP - Test:

class Car:

    def __init__(self, car_details):
        
        self.car_details = car_details

#1:- Calculate insurance 

    def insurance_price(self):

        release_year = self.car_details[0]
        car_price =  self.car_details[1]

        if release_year > 2010 and release_year < 2020:
            
            insurance_price = car_price * 0.05
            
            print("The insurance price is: "+str(insurance_price))

        elif car_price > 6000 and car_price < 17000:
            
            insurance_price = car_price * 0.05

            print("The insurance price is: "+str(insurance_price))
        
        else:

            insurance_price = self.car_details[1] * 0.07
            print("The insurance price is: "+str(insurance_price))
        
        print("\n")

#2:- Check door status

    def check_door(self):

        door = self.car_details[3]

        if door == True:
            print("The door is open!")
        
        elif door == False:
            print("The door is closed!")

        else:
            print('X wrong value inserted X')

#3:- Car details

    def car_data(self):

        car_name = self.car_details[2]
        release_year = self.car_details[0]

        print(f"The model is: {car_name}."+" It was released in the year %s" %release_year+".")

# Instances/Objects:
ford_focus = [2005, 5000, "Ford Foucs", True]

audi_a3 = [2011, 15000, "Audi A3", False]

ford_instance =  Car(ford_focus)

audi_instance = Car(audi_a3)

# Execution:
print("Ford list: ")
ford_instance.car_data()
ford_instance.check_door()
ford_instance.insurance_price()

print("Audi list:")
audi_instance.car_data()
audi_instance.check_door()
audi_instance.insurance_price()