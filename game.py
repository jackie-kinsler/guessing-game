from random import randint

"""A number-guessing game."""

number = randint(1,100)

number_of_guesses = 0

player_name = input("What's your name? ")

print(f"Guess my number, {player_name}, it's between 1 and 100.")

guess = "initialize" 

while guess != number: 
    guess = input("What's your guess? ")
    guess = int(guess)
    if guess < number:
        print("Too Low!")
    if guess > number:
        print("Too High!")
    if guess == number: 
        print("You got it!")



