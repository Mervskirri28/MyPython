import time

my_timer= int(input("Enter the time in seconds: "))

for x in reversed(range(0, my_timer)):
    seconds = x % 60
    minutes = int(x / 60 ) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Times UP!")