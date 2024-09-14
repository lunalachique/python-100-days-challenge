print("Rock, Paper, Scisors game! 🪨🗞️✂️")
print()

Player_1 = input("Player's 1 move. Please enter R, P or S. "
"Note that R = rock, P = paper and S = scissors")
Player_2 = input("Player's 2 move. Please enter R, P or S. "
"Note that R = rock, P = paper and S = scissors")

if Player_1 == "R":
    if Player_2 == "R":
        print("Both players picked Rock. Try again")
    elif Player_2 == "S":
        print("Player 1 took rock and won over Player's 2 Scissors! ")
    elif Player_2 == "P":
        print("Player 2 took paper and won over Player's 1 rock! ")
elif Player_1 == "S":
    if Player_2 == "S":
        print("Both players picked Scissors. Try again")
    elif Player_2 == "R":
        print("Player 2 took rock and won over Player's 1 Scissors!")
    elif Player_2 == "P":
        print("Player 1 took Scissors and won over Player's 2 Paper.")
elif Player_1 == "P":
    if Player_2 == "P":
        print("Both players picked Paper. Try again.")
    elif Player_2 == "R":
        print("Player 1 took Paper and won over Player's 2 Rock.")
    elif Player_2 == "S":
        print("Player 2 took Scissors and won over Player's 1 Paper.")
    else:
        print("Invalid move Player 2. Try again.")
else:
    print("Invalid move Player 1. Try again.")
























#elif (Player_1 != "R" and Player_1 != "S" and Player_1 != "P") and if (Player_2 != "R" and Player_2 != "S" and Player_2 != "P"):
#print("Enter correct value as stated in move note.")