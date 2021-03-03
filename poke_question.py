class SetupQuiz:

    def __init__(self, q_list, number_of_questions):
        import random
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.poke_question = random.randint(0, len(self.question_list)-1)
        self.number_of_questions = number_of_questions
    
    def still_has_question(self):
        return self.question_number < self.number_of_questions
    
    def next_question(self):
        import random
        current_question = self.question_list[self.poke_question]
        self.question_number += 1
        self.poke_question = random.randint(0, len(self.question_list)-1)
        user_answer = input(f'Q.{self.question_number}: What is the type of {current_question.name_poke}? ')
        self.check_answer(user_answer, current_question.type_poke)
    
    def check_answer(self, user_answer, correct_answer):
        split_correct_answer = correct_answer.split()
        if user_answer.lower() in split_correct_answer:
            self.score += 1
            print('You got it right! Nice done!')
        else:
            print("That's wrong. :(")
        print(f'The correct answer was: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}')
        print('\n')