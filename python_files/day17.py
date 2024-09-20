print("Rock, Paper, Scissors game! 🪨🗞️✂️")
print()

counterPL_1 = 0
counterPL_2 = 0 

while True:
    Player_1 = input("Player 1's move. Please enter R, P or S. Note that R = rock, P = paper and S = scissors: ").upper()
    Player_2 = input("Player 2's move. Please enter R, P or S. Note that R = rock, P = paper and S = scissors: ").upper()
    
    if Player_1 not in ["R", "P", "S"]:
        print("Invalid move Player 1. Try again.")
        continue
    if Player_2 not in ["R", "P", "S"]:
        print("Invalid move Player 2. Try again.")
        continue
    
    if Player_1 == "R":
        if Player_2 == "R":
            print("Both players picked Rock. Try again")
        elif Player_2 == "S":
            print("Player 1 took rock and won over Player 2's Scissors!")
            counterPL_1 += 1
        elif Player_2 == "P":
            print("Player 2 took paper and won over Player 1's rock!")
            counterPL_2 += 1
    elif Player_1 == "S":
        if Player_2 == "S":
            print("Both players picked Scissors. Try again")
        elif Player_2 == "R":
            print("Player 2 took rock and won over Player 1's Scissors!")
            counterPL_2 += 1
        elif Player_2 == "P":
            print("Player 1 took Scissors and won over Player 2's Paper.")
            counterPL_1 += 1
    elif Player_1 == "P":
        if Player_2 == "P":
            print("Both players picked Paper. Try again.")
        elif Player_2 == "R":
            print("Player 1 took Paper and won over Player 2's Rock.")
            counterPL_1 += 1
        elif Player_2 == "S":
            print("Player 2 took Scissors and won over Player 1's Paper.")
            counterPL_2 += 1
    
    if counterPL_1 == 3 or counterPL_2 == 3:
        print("Player 1 got", counterPL_1, "wins")
        print("Player 2 got", counterPL_2, "wins")
        if counterPL_1 == 3:
            print("Player 1 won", counterPL_1, "times")
        else:
            print("Player 2 won", counterPL_2, "times")
        exit()