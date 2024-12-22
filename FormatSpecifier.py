#Format Specifier = {value:flags} format a value based on what flags are inserted
#flags are inserted
# used in the context of the f sting usually "print"

# .(number)f = round to that many decimal places (fixed point) decimal point precision
# .(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert space before positive numbers
# :, = comma separator



price1 = 3777.14159
price2 = -9877.65
price3 = 1277.37

# .(number)f = round to that many decimal places (fixed point) decimal point precision
#print(f"Price 1 is ${price1:.1f}")
#print(f"Price 2 is ${price2:.1f}")
#print(f"Price 3 is ${price3:.1f}")

# .(number) = allocate that many spaces (can insert 0 before the number for zero padding)
#print(f"Price 1 is ${price1:10}")
#print(f"Price 2 is ${price2:10}")
#print(f"Price 3 is ${price3:10}") 

# :< = left justify
#print(f"Price 1 is ${price1:<10}")
#print(f"Price 2 is ${price2:<10}")
#print(f"Price 3 is ${price3:<10}")

# :> = right justify
#print(f"Price 1 is ${price1:>10}")
#print(f"Price 2 is ${price2:>10}")
#print(f"Price 3 is ${price3:>10}")

# :^ = center align
#print(f"Price 1 is ${price1:^10}")
#print(f"Price 2 is ${price2:^10}")
#print(f"Price 3 is ${price3:^10}")

# :+ = use a plus sign to indicate positive value
#print(f"Price 1 is ${price1:+}")
#print(f"Price 2 is ${price2:+}")
#print(f"Price 3 is ${price3:+}")

# := = place sign to leftmost position
#print(f"Price 1 is ${price1:=}")
#print(f"Price 2 is ${price2:=}")
#print(f"Price 3 is ${price3:=}")

# :  = insert space before positive numbers
#print(f"Price 1 is ${price1: }")
#print(f"Price 2 is ${price2: }")
#print(f"Price 3 is ${price3: }")

# :, = comma separator
print(f"Price 1 is ${price1:,}")
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")


#mixed or combined
print(f"Price 1 is ${price1:+,.2f}")
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")
