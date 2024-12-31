
#There can be to type of 2D declation

#fruits = ["Apple", "Orange", "Banana"]
#vegetables = ["Celery", "Carrots", "Potatoes"]
#meats = ["Beef", "Chicken", "Pork"]

#groceries = [fruits, vegetables, meats]
#groceries = [["Apple", "Orange", "Banana"], ["Celery", "Carrots", "Potatoes"], ["Beef", "Chicken", "Pork"]] #List of list
#groceries = [("Apple", "Orange", "Banana"), ("Celery", "Carrots", "Potatoes"), ("Beef", "Chicken", "Pork")] #List of Tuple
#groceries = ({"Apple", "Orange", "Banana"}, {"Celery", "Carrots", "Potatoes"}, {"Beef", "Chicken", "Pork"}) #List of Sets
groceries = (("Apple", "Orange", "Banana"), ("Celery", "Carrots", "Potatoes"), ("Beef", "Chicken", "Pork")) #Tuple of Tuples


#print(groceries)

#Nested Loop
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()