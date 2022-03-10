###########################
# Author: Samuel Burke
# Date Created: 03/09/2022
###########################
import requests


def get_questions():
    """
    this function can be replaced with any .JSON data that has a "question" key and a "correct_answer" key,
    so feel free to make the True/False flashcards connect with any True/False JSON. Just keep note, that if your
    .JSON data is arranged differently, you may need to update the QuestionBank initializer.
    :param num: number of questions
    :return: json data of the questions
    """
    return requests.get('https://opentdb.com/api.php?amount=10&type=boolean').json()['results']


# If you would like to add your own questions, use the following format:
# def get_questions():
#     return [
#         {"question": "This is the question1", "correct_answer": "True"},
#         {"question": "This is the question2", "correct_answer": "False"},
#         {"question": "This is the question3", "correct_answer": "True"},
#         {"question": "This is the question4", "correct_answer": "False"},
#         {"question": "This is the question5", "correct_answer": "True"},
#     ]
