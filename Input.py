#input () - A function that prompts the user to enter date
#Retursn the entered data as a string

name = input("What is your name?: ")
#age = input("How old are you?: ")

#We can optimize the code by setting the input to the proper variable that we want
#Example
age = int(input("How old are you?: ")) #This is more readable and takes less line of code.



#Combining the typecasting from the previous sample we can convert the input string into a variable and modify it's value and output when need to display.

#age = int(age) #convert string value into integer first
age = age + 1 #modify the value

print(f"Hello {name}!")
print("Happy Birhtday")
print(f"You are {age} years old") #output the modified variable