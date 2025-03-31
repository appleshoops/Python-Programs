import random

number = random.randint(1, 10)
guess = int(input("Enter a number between 1 and 10 "))
while guess != number:
    if guess > number:
        print("Incorrect guess, guess lower")
        guess = int(input("Enter a number between 1 and 10 "))
    elif guess < number:
        print("Incorrect guess, guess higher")
        guess = int(input("Enter a number between 1 and 10 "))
print("Correct guess!🤑🤑🤑")
