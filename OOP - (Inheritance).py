# OOP - Inheritance:-

# Inheritance allows us to have a class that inherits all the methods and properties of another class

# For exmple:

print("Parent class:\n")

class Vehicle():

    def __init__(self, is_engine_running):
    
        self.is_enginge_running = is_engine_running    
    
    
    def engine_status(self):

        if self.is_enginge_running == True:
            print("The engine is running!")

        elif self.is_enginge_running == False:
            print("The engine is not running!")

        else:
            print("Enter a valid value!")

class PrivateCar(Vehicle):
    
    def __init__(self, is_engine_running):
        self.is_enginge_running = is_engine_running
        super().__init__(is_engine_running)

ford_focus = PrivateCar(True)
ford_focus.engine_status()  