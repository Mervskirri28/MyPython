#Python coumpound interest calulator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle value can't be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("Rate value can't be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the time amount: "))
    if time <= 0:
        print("Time value can't be less than or equal to zero")

#Formula

total = round(principle * pow((1 + rate / 100), time),2)

print(f"Principle Value is: {principle}")
print(f"Rate Value is: {rate}")
print(f"Time Value is: {time}")

print(f"Balance after {time} year/s: ${total:,.2f}")