#Python number guessing game

import random

#Set range
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)


#track random numbers

guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess:")
    
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        
        if guess < lowest_num or guess > highest_num:
            print("WARNING: Range exeed the parameter")
            
        elif guess < answer:
            print("Too low! Try again!")
 
            
        elif guess > answer:
            print("Too high! Try again!")

        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
            
    else:
        print("Invalud entry")
        print(f"Please select a number between {lowest_num} and {highest_num}")