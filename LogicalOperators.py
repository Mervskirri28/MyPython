#Logical Operatos - evaluate multiple condition (or, and, not)
#or - at least one condition must be true
#and - both conditions must be true
#not - inverts the condition (not false, not true)

#Set initial variables value (or)
#temp = -5
#raining = False

#if temp > 35 or temp < 0 or raining:
    #print("Stay inside")
#else:
    #print("Go outside")
    
    
    # and or not sample
temp = 20
sunny = False

if temp >= 28 and sunny:
    print("It is hot and sunny outside")
    print("It is not hot or it is not sunny outside")
elif temp <= 0 and sunny:
    print("It is cold and sunny outside")
    print("It is SUNNY outside")
elif 28 > temp > 0 and sunny:
    print("It is warm outside")
    print("It is SUNNY outside")
if temp >= 28 and not sunny:
    print("It is hot and sunny outside")
    print("It is CLOUDY outside")
elif temp <= 0 and not sunny:
    print("It is cold and sunny outside")
    print("It is CLOUDY outside")
elif 28 > temp > 0 and not sunny:
    print("It is warm outside")
    print("It is CLOUDY outside")

    