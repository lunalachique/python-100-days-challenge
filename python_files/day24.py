print("Infinity Dice")

import random
600
sides = int(input("Enter the number of sides for the dice: "))

def roll_dice():
    while True:
        dice = random.randint(1, sides)
        print("Your rolled", dice)
        again = input("Roll again? (y/n): ")
        if again == "y" or again == "Y":
            continue
        elif again == "n" or again == "N":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")
            break
roll_dice()
