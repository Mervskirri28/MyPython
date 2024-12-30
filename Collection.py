#collection = single "variable" used to store multiple values
#List = [] ordered and changeable. Duplicates OK
#Set = {} unordered and immutable, but Add/Remove OK. No Duplicates
#Turple = () ordered and unchangeable. Duplicated OK. FASTER!

#Collections


#LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST LIST


#fruits = ["Apple", "Orange", "Banana", "Coconut"] #List
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("Apple" in fruits)
#print(fruit[0])

#for fruit in fruits:
#    print(fruit)


#fruits[0] = "Pineapple" #Change Value

#for fruit in fruits:
#    print(fruit)
    
    
#Append an element +
#fruits.append("Pineapple")

#Remove an element -
#fruits.remove("Apple")

#Insert
#fruits.insert(0,"Pineapple")

#Sort
#fruits.sort()

#Reverse
#fruits.reverse()

#Clear
#fruits.clear()

#Index
#print(fruits.index("Apple"))

#Count
#print(fruits.count("Banana"))

#print(fruits)


#SET SET SET SET SET SET SET SET SET SET SET SET SET SET SET SET SET SET SET 

#fruits = {"Apple", "Orange", "Banana", "Coconut"} #Set
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("Apple" in fruits)

#fruits.add("Pineapple")
#fruits.remove("Orange")
#fruits.pop() #Will remove the first element in the set
#fruits.clear()

#print(fruits)


#TUPPLE TUPPLE TUPPLE TUPPLE TUPPLE TUPPLE TUPPLE TUPPLE TUPPLE TUPPLE TUPPLE 


fruits = ("Apple", "Orange", "Banana", "Coconut") #Tuple
#print(dir(fruits))
#print(help(fruits))
#print(len(fruits))
#print("Apple" in fruits)

#print(fruits.index("Apple"))
print(fruits.count("Coconut"))

for fruit in fruits:
    print(fruit)