#Find the hypotenus of a right Triangle

import math

a = float(input("Enter side A:"))
b = float(input("Enter side B:"))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"Side C is {round(c,2)}")