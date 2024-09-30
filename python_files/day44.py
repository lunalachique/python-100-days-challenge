import random

bingo = []
exes = 0
print("\033[33mAlises Bingo Card Generator ⭐️")
print()

def generateNumber():
    return random.randint(1, 90)

def prettyPrint(userInput):
    print(" ┌───────────┬───────────┬───────────┐")
    for i, row in enumerate(bingo):
      is_last_row = i == len(bingo) - 1  
      print(" │", end=" ")
      for j, number in enumerate(row):
          if number == "⭐️BINGO⭐️":
              print(number.center(9), end=" │ ")
          elif userInput == number:
              row[j] = "X"
              print(str(row[j]).center(9), end=" │ ")
          else:
              print(str(number).center(9), end=" │ ")

      print("\n", end="")
      if not is_last_row:
          print(" ├───────────┼───────────┼───────────┤")
      else:
          print(" └───────────┴───────────┴───────────┘")

numbers = []
for i in range(8):
    numbers.append(generateNumber())

numbers.sort()
bingo =  [ [numbers[0], numbers[1], numbers[2]],
           [numbers[3], "⭐️BINGO⭐️", numbers[4]],
           [numbers[5], numbers[6], numbers[7]], ]

for row in bingo:
  for number in row:
    userInput = int(input("What is next number? "))
    prettyPrint(userInput)

exes = 0
for row in bingo:
  for item in row:
    if item=="X":
      exes+=1
      
if exes == 8:
  print("You have won")
else:
  print("Next time")



