# Collections: List, practice (advanced)

# Test 1 : Make A list Named "Employes"
employes = ["Adam" , "John" , "Greg" , "Danna" , "Ashley"]
print("(1) - Print the List: "+str(employes))

# Test 2 : Print The Length Of The List.
print("(2) - Length of the List is  : "+str(len(employes)))

# Test 3 : Replace 'John' with 'Jack' in "Employes" List
employes[1] = "Jack"
print("(3) - Jack added instead of John : "+str(employes))

# Test 4 : Add New Employe in "Employes" List
employes.insert(3 , "Maverick")
print("(4) - Added 'Maverick' to cell '3' : "+str(employes))

# Test 5 : Remove Maverick From The List.
employes.remove('Maverick')
print("(5-a) - Remove 'Maverick' from the list : "+str(employes))

# Test 5-b : Add Maverick to the end of the List
employes.append("Maverick")
print("(5-b) - Add 'Maverick' back to the list : "+str(employes))

# Test 6 : Remove Maverick from the List because he was creating trouble
employes.pop()
print("(6) - Remove Maverick from the Employes : "+str(employes))

# Bonus Assignment : Sort the list by 'abc'
employes.sort()
print("Bonus - Sort the employes : "+str(employes))