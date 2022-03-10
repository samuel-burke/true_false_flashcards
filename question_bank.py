###########################
# Author: Samuel Burke
# Date Created: 03/09/2022
###########################
from question import Question


class QuestionBank:
    """
    Parses the JSON question data and manages a list of Questions
    """
    def __init__(self, json_data):
        """
        Creates a list of Questions assuming the .JSON data has a "question" and "correct_answer" parameter
        :param json_data the question data in .JSON format:
        """
        self.question_number = 0
        self.questions_list = []
        for q in json_data:
            self.questions_list.append(Question(q['question'], q['correct_answer']))

    def still_has_questions(self):
        """
        Checks if the user has retrieved all the loaded questions
        :return: True if there are questions left in the list
        """
        return len(self.questions_list) > self.question_number

    def next_question(self):
        """
        gives the next question in the list
        :return: the next Question in the list of Questions
        """
        question = self.questions_list[self.question_number]
        self.question_number += 1
        return question
