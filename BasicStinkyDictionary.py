# Dictionary Advanced:

# Make a dictionary called 'Office':

fx_members = ['Sarah','Sarim','Rachel','Daniel','Gafoor']
mk_members = ['Guacamole','Pandejo','Cici','Leechi','Levy','Magnus']

office = {'1st Floor':{'Team':"FX",'Members':fx_members},
          '2nd Floor':{'Team':"Marketing",'Members':mk_members}}

print("Welcome to the PussyLickingTM Building :)\nOn the 1st floor, we have our FX team:"
      +str(office['1st Floor']['Team'])+
    ". And on the 2nd Floor we have our marketing team:"+str(office['2nd Floor']['Team']))

# The CEO wants a tour of the second floor:
print("\nThe 2nd floor is assigned to the "+str(office['1st Floor']['Team'])+
      " group.\nOn the members list we have: "+str(office['1st Floor']['Members']))

# The CEO wants a new member in the FX team and he is called Haseeb:
fx_members.append('Haseeb')

print("\nThe addition in the FX team was confirmed and we are happy to welcome Haseeb! "
        +str(office['1st Floor']))

# The CEO wants Cici to be removed from the Marketing team:
mk_members.pop(-4)

print("\nThe changes were done to the Marketing team as per the CEO's request: "
        +str(office['2nd Floor']))

# Remove 2nd Floor:
mk_team = office['2nd Floor'].copy()
office.pop('2nd Floor')

print("The 2nd floor has been demlished and this is the remaning office: "+str(office))

# Move Marketing team over to Floor 1:
office['1st Floor']['Room #2']=[mk_team]

print("\n"+str(office))