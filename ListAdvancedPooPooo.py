# SELF-TEST

# Make a list of all the children calss

students_x=['Rachel','Selina','Ahmed','John','Jack','Haseeb','Jamal','Serim']

# Print out how many students are there in Class X:

print("The name of all the students in Class X : "+str(students_x))

print("The number of students in Class X are : "+str(len(students_x)))

# Correct the name of a children teacher got it wrong:

#CHEATED!~
students_x[7]='Sarim'
print("The students' name has been updated : "+str(students_x))

# A new student joined in July:

students_x.append('Joshua')
print("Welcome the new student : "+str(students_x))

# Rachel left and Jasmine is joining in her place:
students_x[0]='Jasmine'
print("Rachel is unfortunately leaving and we have a replacement : "+str(students_x))

# Sarim is leaving:
students_x.pop(7)
print("Let us all say goodbye to Sarim. You will be missed : "+str(students_x))

# Final number of students:
print("The number of students after Sarim left : "+str(len(students_x)))

#--------------------------------------------------------------------------------------------------#