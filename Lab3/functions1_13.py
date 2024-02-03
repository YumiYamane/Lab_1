import random

def Guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    secret_num = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_num:
            print("\nYour guess is too low.")
        elif guess > secret_num:
            print("\nYour guess is too high.")
        else:
            print(f"\nGood job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

Guess_the_number()