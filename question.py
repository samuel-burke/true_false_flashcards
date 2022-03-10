###########################
# Author: Samuel Burke
# Date Created: 03/09/2022
###########################
import html


class Question:
    """
    Question object to hold the question text and question answer
    """
    def __init__(self, text, answer):
        """
        Creates a Question that holds the fields for the question's message and the correct answer.
        :param text: the string of text for the question
        :param answer: the string "True" or "False"
        """
        self.text = html.unescape(text)
        self.answer = answer
