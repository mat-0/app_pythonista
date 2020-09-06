import random

number = random.randint(1,11)
game = True
tries = 0

while game:
    question = input("Pick an number between 1 and 10 ")
    tries += 1
    try:
        answer = int(question)
        if 1<  answer > 10:
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