import random

const min = 1
const max = 11

number = random.randint(min,max)
game = True
tries = 0

while game:
    question = input(f"Pick an number between {min} and {max-1} ")
    tries += 1
    try:
        answer = int(question)
        if  min <  answer > (max-1):
            print("out of range")
        elif answer == number:
            print(f"you got it! It took {tries} guesses")
            game = False
        elif answer < number:
            print("Your number is too low")
        elif answer > number:
            print("Your number is too high")
    except ValueError:
        print("that is not a number")
        continue

print(f"The number that was: {number}")