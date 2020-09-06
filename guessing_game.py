import random

MIN_VALUE = 1
MAX_VALUE = 10
number = random.randint(MIN_VALUE,MAX_VALUE)
game = True
tries = 0

while game:
    question = input(f"Pick an number between {MIN_VALUE} and {MAX_VALUE} ")
    tries += 1
    try:
        answer = int(question)
        if  MIN_VALUE <  answer > MAX_VALUE:
            print("out of range! please try again")
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