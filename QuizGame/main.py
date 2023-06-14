from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question = item["text"]
    answer = item["answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.still_has_questions():
    new_quiz.question_number()

print("You have completed the challenge")
print(f"Your final score is: {new_quiz.score}/{new_quiz.question} ")
