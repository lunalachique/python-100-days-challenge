print("Math Game")
print()

score = 0

while True:
    numberMult = int(input("Enter a number that you want to learn how to multiply from 1 to 10."))
    for i in range(1, 11):
        correctAnswer = numberMult * i
        print(i, "x", numberMult, "=")
        userAnswer = int(input("Enter correct anser for this equation."))
        if userAnswer == correctAnswer:
            print("Correct", userAnswer, "is the correct answer.")
            score += 1
        else:
            print("Incorrect", userAnswer, "is not the correct answer. Correct answer is", correctAnswer, ".")
    if score == 10:
        print("Congratulations! You got all 10 questions correct.")
    else:
        print("You got", score, "questions correct out of 10.")


    