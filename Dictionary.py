#Dictionary = a collection of {key.value} pairs
#ordered and changeable. No Duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("USA"))


#if capitals.get("Russia"):
#    print("That capitals exists")
#else:
#    print("That capital doesn't exist")

#capitals.update({"Germany": "Berlin"}) #Insert new key or update key value pair
#capitals.update({"USA": "New York"})
#capitals.pop("China") #Delete a pair
#capitals.popitem() #Will remove the latest key value pair wihin the Dictionary
#capitals.clear() #Clear the Dictionary
#keys = capitals.keys() #Get All the keys within the Dictionary but not the values

#for key in capitals.keys():
#    print(key)

#values = capitals.values()

#print(values) #Get All the values within the Dictionary but not the keys

#for value in capitals.values():
#    print(value)


#items = capitals.item()

#print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")