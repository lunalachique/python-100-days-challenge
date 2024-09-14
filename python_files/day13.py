print("Your Grade Generator")
print()
name = input("Name of exam: ")
print()
ExamPoints = int(input("How many points did you get in this exam? "))
TotalPoints = 100
PercentPoints = round(ExamPoints *100 / TotalPoints,2)
if PercentPoints >= 90 and PercentPoints <=100:
    print("You have got", PercentPoints ," % on the test and got grade A+ ❤️")
elif PercentPoints >= 80 and PercentPoints < 90:
    print("You have got", PercentPoints ,"% on the test and got grade A- ✌️")
elif PercentPoints >= 70 and PercentPoints < 80:
    print("You have got", PercentPoints ,"% on the test and got grade B 😊")
elif PercentPoints >= 60 and PercentPoints <70:
    print("You have got", PercentPoints ,"% on the test and got grade C ✌️")
elif PercentPoints >= 50 and PercentPoints <60:
    print("You have got", PercentPoints ,"% on the test and got grade D ✌️")
elif PercentPoints >= 0 and PercentPoints < 40:
    print("You have got", PercentPoints ,"% on the test and got grade U 😒")
else:
    print("Please check if you have entered correct value.")
