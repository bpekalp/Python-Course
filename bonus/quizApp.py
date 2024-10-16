import json

with open("bonus/files/quiz.json") as file:
    quizStr = file.read()

quiz = json.loads(quizStr)

correctAnswers = 0

for index, question in enumerate(quiz, start=1):
    print(question["questionText"])

    for choice in question["choices"]:
        print(choice)

    userAnswer = input("Enter your answer: ").strip().upper()
    question["userAnswer"] = userAnswer

    if question["userAnswer"] == question["answer"]:
        correctAnswers += 1

    print()


totalQuestions = index
totalScore = float(correctAnswers / totalQuestions) * 100

for index, question in enumerate(quiz, start=1):
    result = "incorrect."

    if question["userAnswer"] == question["answer"]:
        result = "correct!"

    print(question["questionText"])
    print(f"Your answer for this question was {result}")
    print(f"Answer was: {question["answer"]}, you picked {question["userAnswer"]}.")
    print()

print(f"Correct answers: {correctAnswers}/{totalQuestions}")
print(f"Total score: {totalScore:.2f}")
