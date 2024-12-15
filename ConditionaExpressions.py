#Conditional Expressions - A one-line shortcut for the if-else statement (ternary operator)
#Print or assign one of two values based on a condition
# X if condition else Y


num = 7
a = 10
b = 7
age = 29
temperature = 30
user_role = "admin"

#print("Positive" if num > 0 else "Negative") # check if num is greater than 0, if true print "Positive", if false print "Negative"

#result = "EVEN" if num % 2 == 0 else "ODD" #check if num is even or odd
#max_num = "Greater" if a > b else "Lesser"
#max_num = a if a > b else b
#min_num = "Greater" if a < b else "Lesser"
#min_num = a if a < b else b

#print(max_num)
#print(min_num)


#status = "Adult" if age >= 18 else "Teen"
#print(status)

#weather = "Hot" if temperature >= 25 else "Cold"

#print(weather)

access_level = "Super User" if user_role == "admin" else "Client User"

print(access_level)