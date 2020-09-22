from random import randint
"""A number-guessing game."""

# Put your code here

print("I'll guess your number... give me a number between 1 and 100.")
 
player_name = input("What's your name? ")

guess = -100  #initialize guess value 

print(player_name)

number = randint(1,100)
print(number)
# print(type(number))