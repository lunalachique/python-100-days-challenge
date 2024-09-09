print("Generation identifier. ")
print()
yourGen = int(input("Which year you were born? "))
if yourGen >= 1925 and yourGen <= 1945:
    print("You are from Silent Generation")
elif yourGen >=1946 and yourGen <=1964:
    print("You are Baby Boomer! ")
elif yourGen >= 1965 and yourGen <= 1980:
    print("You are GENERATION X! ")
elif yourGen >= 1981 and yourGen <= 1996:
    print("You are Millenial! ")
elif yourGen >=1997 and yourGen <= 2012:
    print("YOu are GEN Z!")
elif yourGen >=2012 and yourGen <=2024:
    print("You are Generation Alpha!")
else:
    print("Who are you? ")