# 1 - Make A Dictionary

Alex = {'Age' : 32 , 'Married' : "Yes" , 'Kids' : 3}
print("1 - This Is Alex : "+str(Alex))

# 2 - Print Every Variable 

age = Alex["Age"]
married = Alex["Married"]
kids = Alex["Kids"]

print("2 -\nAlex is "+str(age)+" years old.\nIs Alex married ? "+married+".\nAlex has "+str(kids)+" kids.")
print("All values printed by putting them into a variable.")

# 3 - Update Alex Age

alex_age = {'Age' : 33}
Alex.update(alex_age)
print("2 - Update Alex Age To '33' : "+str(Alex))

# 4 - Update Alex Kids

alex_kids = {'Kids' : 4}
Alex.update(alex_kids)
print("3 - Update Alex's Kids : "+str(Alex))

# 5 - Print out the values of the dictionary

print("4 - Print out the values of the dictionary : "+str(Alex.values()))

# 6 - Print out the Keys of the dictionary

print("5 - Print out the Keys of the dictionary : "+str(Alex.keys()))