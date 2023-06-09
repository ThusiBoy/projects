import random

HARD = 5
EASY = 10

def check_number(guess_number, answer, turns):
    if guess_number == answer:
        print(f"you got it, answer is {answer}")
    elif guess_number < answer:
        print("too low")
        return turns - 1
    else:
        print("too high")
        return turns - 1

def diffuclty_level():
    level = input("Choose a difficulty. Type 'hard' or 'easy': ")
    if level == "hard":
        return HARD
    else:
        return EASY

def game():
    print("Welcome to Guess number Game")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    turns = diffuclty_level()

    guess = 0
    while guess != answer:
        print(f"you have {turns} remaining to guess a number")

        guess_number = int(input("Make a guess: "))
        turns = check_number(guess_number, answer, turns)

        if turns == 0:
            print("you have run out of guesses, you lose!")
            return
game()
