# Simple car dealership dialogue by Beeb :3

# Global variables:
kind = str
price_range = int
seats = int
transmission = str
car = str

# First dialogue:

what = input("Hello, Sir! Welcome to PooPoo Motors. How can I help you today ? ")

if what == 'car':
    kind = input("What kind of vehicle are you looking for ?\n"+
                 "Here's a list of cars in our catalogue: \n"+
                 'Sedan\n'+
                 'Suv\n'+
                 'Sports Car\n'+
                 "You may choose one: ")
    
    if kind == 'Sedan':
        price_range = int(input("Sweet! What is your price range ? "))

        if price_range > 6000 and price_range < 20000:
            seats = int(input("Great! How many seater would you like your vehicle to be ? "))

            if seats == 4:
                transmission = input("Mmm would you like manual or automatic transmission? ")
                car = input('Awesome! These are the available vehicles: \n'+
                                "Poop Stain\n"+
                                "Shitty Tart\n"+
                                "Slimy Bob\n"+
                                "You may pick one: ")    

            elif seats == 2:
                transmission = input("Mmm would you like manual or automatic transmission? ")
                car = input('Awesome! These are the available vehicles: \n'+
                                "Poop Stain\n"+
                                "Shitty Tart\n"+
                                "Slimy Bob\n"+
                                "You may pick one: ")             

            else:
                print("We are sorry! We don't have such vehicles.")       
        
        else:
            print("We don't really have any machine to entertain you!")

    elif kind == 'Suv':
        price_range = int(input("Sweet! What is your price range ? "))

        if price_range > 6000 and price_range < 20000:
            seats = int(input("Great! How many seater would you like your vehicle to be ? "))

            if seats == 4:
                transmission = input("Mmm would you like manual or automatic transmission? ")
                
                if transmission == 'Manual':
                    car = input('Awesome! These are the available vehicles: \n'+
                                "Poop Stain\n"+
                                "Shitty Tart\n"+
                                "Slimy Bob\n"+
                                "You may pick one: ")    
                
            elif seats == 2:
                transmission = input("Mmm would you like manual or automatic transmission? ")
                car = input('Awesome! These are the available vehicles: \n'+
                                "Poop Stain\n"+
                                "Shitty Tart\n"+
                                "Slimy Bob\n"+
                                "You may pick one: ")    
            
            else:
                print("We are sorry! We don't have such vehicles.")

        else:
            print("We don't really have any machine to entertain you!")
    
    elif kind == 'Sports Car':
        price_range = int(input("Sweet! What is your price range ? "))

        if price_range > 6000 and price_range < 20000:
            seats = int(input("Great! How many seater would you like your vehicle to be ? "))

            if seats == 4:            
                transmission = input("Mmm would you like manual or automatic transmission? ")
                car = input('Awesome! These are the available vehicles: \n'+
                                "Poop Stain\n"+
                                "Shitty Tart\n"+
                                "Slimy Bob\n"+
                                "You may pick one: ")    

            elif seats == 2:
                transmission = input("Mmm would you like manual or automatic transmission? ")
                car = input('Awesome! These are the available vehicles: \n'+
                                "Poopy Doopy\n"+
                                "Ferrari\n"+
                                "Lamborghini\n"+
                                "You may pick one: ")    

            else:
                print("We are sorry! We don't have such vehicles.")
                
        else:
            print("We don't really have any machine to entertain you!")            
    
    else:
        print("Enter a valid car name!")

else:
    print("This is a car dealership, sir!")


class CarBuilder:

    def __init__(self, kind, price, seats, transmission, car):
        self.kind = kind
        self.price = price
        self.seats = seats
        self.transmission = transmission
        self.car = car

    def car_name(self):

        print(f"The car is {self.car}.")

    def car_kind(self):

        print(f"It's picked a {self.kind}.")

    def car_price(self):

        print(f"It costed you ${self.price}.")

    def car_seats(self):

        print(f"It is a {self.seats} seater car.")

    def car_transmission(self):
        
        print(f"Your car is a {self.transmission}")

print("\n")
print("Below are the details of your new purchase!")
car_list = CarBuilder(kind, price_range, seats, transmission, car)

car_list.car_name()
car_list.car_kind()
car_list.car_seats()
car_list.car_transmission()
car_list.car_price()