import random

number = random.randint(1,11)
game = True

while game:
    question = input("Pick an number between 1 and 10 ")
    try:
        answer = int(question)
        if answer < 1 or answer > 10:
            print("out of range")
        elif answer == number:
            print("you got it!")
            game = False
        elif answer < number:
            print("Your number is too low")
        elif answer > number:
            print("Your number is too high")
    except ValueError:
        print("that is not a number")
        continue

print("The number that was: ", number)