###########################
# Author: Samuel Burke
# Date Created: 03/09/2022
# https://youtu.be/rEs39q4uRBg
###########################
import data
from question_bank import QuestionBank
from quiz_ui import QuizUI


def main():
    """
    Collects the raw data and launches the GUI
    """
    json_data = data.get_questions()
    bank = QuestionBank(json_data)
    QuizUI(bank)


if __name__ == "__main__":
    main()
