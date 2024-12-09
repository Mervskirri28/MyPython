#Typecasting - the process of converting a variable from one date type to another
# str(), int(), float(), bool()

name = "Mervskirri"
age = 29
gpa = 3.2
is_student = True

#output every variables

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

#typecast every variable
gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
#check if output becomes string
print(type(age))


name = bool(name)
print(name)

#converting variable behave different when converting strings just add. while interger uses the mathimatical logic.