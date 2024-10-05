print("Character health STAT generator")
print()

import random

def Rolldice(sides):
    rolled = random.randint(1, sides)
    return rolled

def roll_stats():
    roll6 = Rolldice(6)
    roll8 = Rolldice(8)
    health = roll6 * roll8
    return health

again = "y"

while again == "y" or again == "Y":
    characterName = input("Enter your character's name: ")
    health = roll_stats()
    print("Your character", characterName, "health is", health)
    again = input("Do you want to generate another character's health? (y/n): ")
    print()
print("Goodbye!")
