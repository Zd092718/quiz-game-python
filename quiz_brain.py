class QuizBrain:
    def __init__(self, questions_list):
        self.questions_number = 0
        self.questions_list = questions_list

    def still_has_questions(self):
        return self.questions_number < len(self.questions_list)


    def next_question(self):
        current_question = self.questions_list[self.questions_number]
        self.questions_number += 1
        input(f"Q.{self.questions_number}: {current_question.text} (True/False):")