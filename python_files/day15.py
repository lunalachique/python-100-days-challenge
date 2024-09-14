print("The sounds of animals!")
print()

exit = "no"

while exit.lower() != "yes":
    animal = input("What animal do you want to chose?")
   
    if animal == "cow" or animal == "Cow":
        print(animal, "sounds moo! 🐮")
    elif animal == "cat" or animal == "Cat":
        print(animal, "sounds meow 🐱")
    elif animal == "dog" or animal == "Dog":
        print(animal, "sound Woof 🐶")
    elif animal == "sheep" or animal == "Sheep":
        print(animal, "sounds Beee 🐑")
    elif animal == "pig" or animal == "Pig":
        print(animal, "sound Oink 🐷")
    elif animal == "duck" or animal == "Duck":
        print(animal, "sounds Quack 🦆")
    else:
        print("I do not know this animal. Try to type another one.")
    
    exit = input("Do you want to continue? (yes/no) ")
