print("List Generator")
print()
startNr = int(input("Enter the starting number: "))
endNr = int(input("Enter the ending number: "))
step = int(input("Enter the step size between numbers: "))

for i in range(startNr, endNr+1, step):
    print(i)
    