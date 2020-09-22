from random import randint
"""A number-guessing game."""

print("Guess my number, it's between 1 and 100.")
 
player_name = input("What's your name? ")

guess = -100  #initialize guess value 

number = randint(1,100)

while guess != number: 
    guess = input("What's your next guess?")
    if guess < number:
        print("Too Low!")
    if guess > number("Too High!")
    if guess == number: 
        print("You got it!")