print("How many seconds in a year")

year = int(input("Enter the year: "))
days = 365
hours =24
minutes=60
seconds=60

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
    leapYearRes = ((days + 1) * hours * minutes * seconds)
    print(" In a year", year,"there was", leapYearRes, "seconds!")
else:
    print(year, "is not a leap year")
    YearRes = (days * hours * minutes * seconds)
    print(" In a year", year,"there was", YearRes, "seconds!")
