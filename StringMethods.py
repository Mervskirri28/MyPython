#Useful Stings Methods

#name = input("Enter your Full name: ")

#result = len(name) #"len" funtion measure the number of strings
#result = name.find("M")
# #the DOT can call a method and the "Find" method will find the first accurance of the string and it's position when used. The index will always starts on 0.
#That's why the result will be different if we don't increment the number value of the string before printing.

#result = name.rfind("s")
#the DOT can call a method and the "rFind" method will find the last accurance of the string and it's position when used. The index will always starts on 0.
#That's why the result will be different if we don't increment the number value of the string before printing.

#print(f"The position of String is on: {result}")

#name = name.capitalize() #will capitalize the first character
#name = name.upper() #upper case all letters within the string
#name = name.lower() #lower case all letters within the string
#name = name.isdigit() #will check the string if contains or all number. the return is a boolean
#name = name.isalpha() #will check the string if contains all letters. the return is a boolean


#phnone_number = input("Enter your phone number: ")

#Let's count how many dashes within the input of number
#result = phnone_number.count("-")
#result = phnone_number.replace("-", " ") #will replace the target character with specified character we indicated (we can also iliminate the space with blank character so no spaces "")

#print(result)

#Learn more using the help method

print(help(int))