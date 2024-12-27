#for loop = execute a block of code a fixed number of times.
# You can iterate a range, string, sequence, etc.

#Basic syntax

#for x in range(1, 11):
#    print(x)

#Addutional

#for x in reversed(range(1, 11)):
#    print(x)
#print("HAPPY NEW YEAR!")


#for x in range(1, 11, 2): #Added Steps
#    print(x)
#print("HAPPY NEW YEAR!")

#credit_num = "1230-4560-7890-0000"

#for x in credit_num:
#   print(x)


#for x in range(1, 21): #continue is skipping
#    if x == 13:
#        continue
#    else:
#        print(x)

for x in range(1, 21): #break stops the cycle
    if x == 13:
        break
    else:
        print(x)
