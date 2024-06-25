# Gather information from the user and put it inside a Dictionary and print it as an ID Card:

# Making the program:
print("Hello and welcome to Digital Identity Theft forum.\n\nWhere we collect your information and sell it for a fortune. PLease give us all your info donw below :)")

# Take info:

name = input("So what is your name ? ")

age = input("What is your age ? ")

sex = input("Gay or straight ? ")

gender = input("Mhm Gender identity lmao ? ")

language = input("What is your mommas tongue ? ")

id_card = {'Name':name , 'Age':age , 'Sex':sex , 'Gender':gender , 'Language':language}

# Copy the newly added info to a new dictionary:
id_card_cop1 = id_card.copy()
id_card_cop2 = {}
id_card_cop3 = {}

# Print out the ID CARD:
print("HERE IS YOUR ID CARD: \nName: "+id_card_cop1["Name"]+".\nAge: "+id_card_cop1["Age"]+".\nSex: "+id_card_cop1["Sex"]+".\nGender: "+id_card_cop1["Gender"]+".\nLanguge: "+id_card_cop1["Language"]+".")

"Thanks for giving us all your information lmfao"