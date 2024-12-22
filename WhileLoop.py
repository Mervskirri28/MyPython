#while loop = execute some code While some condition remains true


name = input("Enter your name: ")

while name == "":
    print("Error! No submitted entry")
    name = input("Enter your name: ")
print(f"Welcome {name}")