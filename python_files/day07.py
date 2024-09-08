print("Let's detect if you are a superfan of 'One Piece' or not?")
print()
print("Answer these questions to find out:")

anime = input("What is your favorite anime? ")
if anime == "One Piece":
    print("Perfect Choice!")
    character = input("What is your favorite character? ")
    
    if character == "Luffy":
        print("Oh yeah, everyone loves Luffy 👒")
        LuffyPartner = input("Who was Luffy's partner? ")
        if LuffyPartner == "Boa Hancock":
            print("Correct! You are a true fan! ❤️")
        else:
            print("You should watch more One Piece!")
    
    elif character == "Chopper":
        print("Chopper is soooo cute!~~ 🦌")
        ChopperName = input("What is Chopper's full name? ")
        if ChopperName == "Tony Tony Chopper":
            print("Fantastic! You are a true fan!")
        else:
            print("Incorrect, please start again! 😒")
    
    elif character == "Ace":
        print("Gold. D. Ace, nice choice. 🍖")
        AceDad = input("Who was Ace's father? ")
        if AceDad == "Gol D. Roger":  # Corrected name format
            print("You are a superfan!! Congrats! ❤️")
        else:
            print("Incorrect! Try again.")

    else:
        print("Let's talk about other characters.")
else:
    print("You should definitely watch One Piece. 🍖🦌👒❤️")

