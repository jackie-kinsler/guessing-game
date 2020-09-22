from random import randint

"""A number-guessing game."""

number = randint(1,100)

number_of_guesses = 0

player_name = input("What's your name? ")

print(f"Guess my number, {player_name}, it's between 1 and 100.")

guess = "initialize" 

def check_within_range(value):
    if value < 1 or value > 100:
        print("I said between 1 and 100.")

while guess != number: 
    guess = input("What's your guess? ")
    number_of_guesses += 1
    guess = int(guess)
    if guess < number:
        print("Too Low!")
    if guess > number:
        print("Too High!")
    check_within_range(guess)
    if guess == number: 
        print(f"You got it in {number_of_guesses} guesses!")



