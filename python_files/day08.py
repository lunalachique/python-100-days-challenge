print("Daily Affirmation Generator")
print()
name = input("What is your name? ")

if name.lower() == "diana":
    mood = input("What is your mood today? ").lower()
    print(f"Debug: name = {name}, mood = {mood}")  # Debugging line
    if mood == "bad":
        print("Dear", name, ". Even though things feel tough right now, you are capable of overcoming challenges.")
    elif mood == "normal":
        print("Dear", name, ". You are resilient, and no challenge is too big for you to overcome.")
    elif mood == "good":
        print("Dear", name, ". Your happiness is well-deserved, and it’s a reflection of all the good you bring into the world.")
    else:
        print("I need to know your mood, so I can support you, ", name)
else:
    print("I do not know your name, but still, I hope that you’re full of inspiration and light, keep riding that wave!")


# if name == "diana" or "Diana":
print("Daily Affirmation Generator")
print()
name = input("What is your name? ")

if name == "Diana" or name == "diana":
    mood = input("What is your mood today? ")
    if mood == "Bad" or mood == "bad":
        print("Dear", name, ". Even though things feel tough right now, you are capable of overcoming challenges.")
    elif mood == "Normal" or mood == "normal":
        print("Dear", name, ". You are resilient, and no challenge is too big for you to overcome.")
    elif mood == "Good" or mood == "good":
        print("Dear", name, ". Your happiness is well-deserved, and it’s a reflection of all the good you bring into the world.")
    else:
        print("I need to know your mood, so I can support you, ", name)
else:
    print("I do not know your name, but still, I hope that you’re full of inspiration and light, keep riding that wave!")