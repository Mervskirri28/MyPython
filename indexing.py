#indexing = accessing elements of sequence using [] (indexing operator)
#[start : end : step]

credit_number = "1234-5678-9012-3456"

#computer indexing always starts with "0"
#print(credit_number[0])
#print(credit_number[:4]) #start up to the forth index
#print(credit_number[5:9])
#print(credit_number[5:]) #fith up to the last index
#print(credit_number[-1]) #Will print from the end of the string because of the negative value
#print(credit_number[::2]) #step will count every next index value you input for this example every (2)

#Two solutions for getting the last 4 digit of the back number
#last_digits = (credit_number[15:])
last_digits = (credit_number[-4:])

print(f"Your last credit card number are {last_digits}")