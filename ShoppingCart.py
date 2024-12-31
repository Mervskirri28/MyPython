#Shopping Cart Program


foods = []
prices = []
total = 0

print("Welcome to your Shopping Cart!\n")

while True:
    food = input("Enter a food to buy(Press q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print()
print("*******YOUR CART*******")
for food in foods:
    print(food)
    
for price in prices:
    total += price

print(f"With a total of ${total:,.2f}")