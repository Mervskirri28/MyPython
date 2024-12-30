#Nested loop = A loop within another loop (outer, inner)
#outer loop:
#inner loop:

#Sample of loops

#x = -1
#y = 5

#while x > 0:
#    while y > 0:
#        print("Do Nothing")
        
        
#for x in range(3):
#    for y in range(9):
#        print("Do Nothing")
        
#while x > 0:
#    for y in range(9):
#        print("Do Nothing")
        
#for x in range(3):
#    while y > 0:
#        print("Do Nothing")

#for x in range(3):
#    for y in range(1, 10): #10 is exclusive
#        print(y, end =" - ")
#   print()

#print rectangle

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns): #10 is exclusive
        print(symbol, end ="")
    print()