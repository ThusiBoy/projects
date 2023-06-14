class QuizBrain:
    def __init__(self,questions_list):
        self.question = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        return self.question < len(self.questions_list)

    def question_number(self):
        current_question = self.questions_list[self.question]
        self.question += 1
        user_answer = input(f"Q.{self.question}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!.")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your currect score is : {self.score}/{self.question}.")
        print("\n")


