#!/usr/bin/python3
from random import randint

secretNumber = randint(1,20)
print("I am thinking of a number between 1 and 20.")


# Ask the playuer to guess 6 times.
for guessesTaken in range(1,7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in {} guesses!'.format(guessesTaken))
else:
    print('Nope. The number I was thinking of was {}'.format(SecretNumber))

