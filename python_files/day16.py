print("Fill-in the blank lyrics!")
print()

counter = 1
while True:
    lyrics = input("Mr. _____ , bring me a dream")
    if lyrics == "sandman" or lyrics == "Sandman":
        print("Correct!", lyrics,"is correc word!")
    else:
        print("Try again.", lyrics,"is not correct word.")
        counter +=1
    if lyrics == "Sandman" or lyrics == "sandman":
        break
print("Well done, it only took you" ,counter, "atempts" )
