#validate user input exercise
#username is no more than 12 characters
#username must not contain spaces
#username must not contain digits


username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can't exceed 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username must not containt numbers")
else:
    print(f"Welcome {username}")