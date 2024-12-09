#Exercuese 2 Shopping cart program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: $"))
quantity = int(input("How many would you like?: "))

#Execute calculation
tmp_total = price * quantity #I added internal calculation if incase the decimal points has more length in the output
total = round(tmp_total,2)  #transfer internal calculation into actual variable that will output the value rounding it of.


print(f"The total price for the {quantity}pcs of {item} is: ${total}")