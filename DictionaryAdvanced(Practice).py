# Dictionary Practice (Advanced):

# Task 1 - Create a nested dictionary and give it the name "building_attendants":
#          And add two parent keys: floor1 and floor2.
building_attendants = {"Floor 1":{"1st Appartment":'Rachel',"2nd Appartment":'Jeen'} , 
                       "Floor 2":{"3rd Appartment":'Jack'}}

print("(1) - All the appartments and tenants in living in them :"+str(building_attendants))

# Task 2 - Print out the people living in "Floor 1":

print("\n(2) - The tenants of Floor 1 in Fajar Colony: "+str(building_attendants["Floor 1"]))

# Task 3 - Print out the residents of 2nd Appartmnet:

print("\n(3) - The owner wants to know lives in the 2nd Appartment. Her name is: "+
      str(building_attendants["Floor 1"]["2nd Appartment"]))

# Task 4 - There is a new appartment on the second floor and Carrol just moved in there:
building_attendants["Floor 2"]["4th Appartment"] = 'Carrol'

print("\n(4) - There is a new appartment on the 2nd floor and a new tenant just moved in: "+
      str(building_attendants))

# Task 5 - Remove appartment 1 from the dictionary because the owner gave it to his daughter:
building_attendants["Floor 1"].pop("1st Appartment")

print("(5) - The 1st appartment is no longer on lease : "+str(building_attendants))