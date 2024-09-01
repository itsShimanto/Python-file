questions = ("1.A is the right answer.Type A: ",
             "2.C is the right answer.Type C: ",
             "3.D is the right answer.Type D: ",
             "4.B is the right answer.Type B: ",
             "5.C is the right answer.Type C: ")

opetions = (("A.Correct","B.Wrong","C.Wrong","D.Wrong"),
            ("A.Wrong","B.Wrong","C.Correct","D.Wrong"),
            ("A.Wrong","B.Wrong","C.Wrong","D.Correct"),
            ("A.Wrong","B.Correct","C.Wrong","D.Wrong"),
            ("A.Wrong","B.Wrong","C.Correct","D.Wrong"))

question_num = 0
guesses = []
guessed_right = []
score = 0
answers = ("A","C","D","B","C")

for question in questions:
  print("------------------------------------")
  print(question)
  for opetion in opetions[question_num]:
    print(opetion)
  guess = input("Enter your answer: ").upper()
  guesses.append(guess)
  if guess == answers[question_num]:
    print("Correct!")
    guessed_right.append(guess)
  else:
    print("Incorrect!")
  question_num += 1
print("------------------------------------")
print(f"Your guesses {guesses}")
print(f"Correct answers {answers}")

score = int((len(guessed_right) / 5) * 100)
print("Your score is " + str(score))

if score == 0:
  print("Wow you're dumb!")
print("------------------------------------")