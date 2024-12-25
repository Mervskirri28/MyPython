#while loop = execute some code While some condition remains true


#name = input("Enter your name: ")

#while name == "":
   # print("Error! No submitted entry")
   # name = input("Enter your name: ")
#print(f"Welcome {name}")


#--------------------------------------------------

#age = int(input("Enter your age: "))

#while age < 0:
    # print("Age can't be negative")
    # age = int(input("Enter your age: "))
#print(f"You are {age} year old")

#--------------------------------------------------

#food = input("Enter a food you like (press q to quit): ")

#while not food == "q":
    #print(f"You like {food}")
    #food = input("Enter a food you like (press q to quit): ")
#rint("Bye")

#--------------------------------------------------

num = int(input("Enter a # between 1 - 10: "))

while num <1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
print(f"Your number is {num}")