#Variables - A container for a value (string, integer,float,boolean).
#A variable behaves as if it was the value it contains.

#String Variable
first_name = "Bro"
food = "shawarma"
email = "sharwarmaBro@fake.com"


print(first_name)
#insert variation
print(f"Hello {first_name}")
print(f"I like {food}")
print(f"My email is: {email}")

#Integer Variables
age = 29
quantity = 7
num_of_students = 77

#inset variation
print(f"I am {age} years old")
print(f"You age buying {quantity}")
print(f"The number of studetns are {num_of_students}")

#Floating Numbers

price = 11.99
gpa = 3.2
distance = 7.7

#insert varation
print(f"The price is $ {price}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance}km")

#Boolean

is_student = True
for_sale = True
if_online = False

#insert variation
if is_student:
    print("You are a student")
else:
    print("You are not a Student")
    
    
if for_sale:
    print("This item is for sale")
else:
    print("This item is not availabe")
    
if if_online:
    print("You are online")
else:
    print("You're offline please check your network")
    