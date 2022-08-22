from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    q_to_add = Question(question["text"], question["answer"])
    question_bank.append(q_to_add)

q_brain = QuizBrain(question_bank)

while q_brain.still_has_questions():
    q_brain.next_question()

print("You've completed the quiz!")
print(f"Your final score was {q_brain.score} out of {q_brain.question_number}")

