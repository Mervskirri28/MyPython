#Python Quiz

#Declare variables

questions = ("[QUESTION] What is the largest planet in our solar system?: ",
             "[QUESTION] What is the main source of energy for Earth?: ",
             "[QUESTION] How many legs does a spider have?: ",
             "[QUESTION] What is the freezing point of water?: ",
             "[QUESTION] What is the smallest unit of matter?")

options = (("A. Jupiter", "B. Earth", "C. Mercury", "D. Venus"),
           ("A. Water", "B. Air", "C. Sun", "D. Moon"),
           ("A. 12 Legs", "B. 9 Legs", "C. 8 Legs", "D. 26 Legs"),
           ("A. 32", "B. 5", "C. 4", "D. 0"),
           ("A. cm", "B. atom", "C. meter", "D. ft"))

answer = ("A", "C", "C", "D", "B")
guesses = []
score = 0
question_num = 0
totalscore = 0

print("\nWELCOME TO PYTHON QUIZ!\n\n[INSTRUCTION] Pleast start answering the following questions. Select in the option and press enter. \n")
for question in questions:
    print("****************************************\n")
    print(f"{question} [{question_num + 1}/5]\n\n")
    for option in options[question_num]:
        print(option)
        print("\n")
    
    guess = input("Enter (A, B, C or D): ").upper()
    guesses.append(guess)
    
    if guess == answer[question_num]:
        score += 1
        print("\n")
        print("YOU GOT THE CORRECT ANSWER!\n")
    else:
        print("\n")
        print(f"INCORRECT ANSWER! - {answer[question_num]} is the CORRECT ANSWER")
        print("\n")
    question_num += 1 #Question Number will increment in order to proceed to the next question.

#Print Summary of the Quiz

print("*******************************\n\nQUIZ SUMMARY\n")
print("[CORRECT ANSWERS] ", end="")
for answers in answer:
    print(answers, end=" ")

print("\n[GUESSES] ", end="")
for guess in guesses:
    print(guess, end=" ")

totalscore += score
percentage = int(score / len(questions) * 100)
print(f"\n\nTHANK YOU FOR TAKING THE QUIZ\nYOUR TOTAL SCORE IS {totalscore}/{question_num} = {percentage}%\n\n*******************************")
if totalscore <= 3:
    print("\n[NOTE] PRACTICE MORE\n")
else:
    print("\n[NOTE] YOU ARE GREAT!\n")