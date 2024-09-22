print("Loan Calculator")
print()

loan = int(input("Enter your loan amount: "))
percent = 0.05
year = 0
loanNew = int(loan)
for year in range(10):
    loanNew += float(loanNew * percent)
    print("Year", year+1, "is", round(loanNew, 2))
print()
print("In total you will need to pay", round((loanNew - loan), 2), " $ interest for your loan after 10 years.")

