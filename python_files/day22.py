print("Random Number Generator")
print()

import random

correctNum = random.randint(1, 10)
attempt = 1

while True:
    guess = int(input("Guess a number between 1 and 1,000,000: "))
    if guess > correctNum and guess <= 1000000:
        print("Chosen number", guess, "is too high! Try another one.")
        attempt +=1
    elif guess > 0 and guess < correctNum:
        print("Cosen number", guess, "is too low. Try another one.")
        print(correctNum, guess)
        attempt +=1
        continue
    elif guess == correctNum:
        print(guess, "is correct number! You won!")
        break
    elif guess <= 0:
        print("This game is over for you. ☠️")
        print(correctNum, guess)
        exit()
    else:
        print("Please choose number from 1 to 1,000,000!!")
        attempt +=1
print("It took you", attempt, "attempt`s to guess the number! 😊")
