###########################
# Author: Samuel Burke
# Date Created: 03/09/2022
###########################
from tkinter import *
import tkmacosx
import pygame

GREEN = {"idle": "#9bdeac", "hover": "#85d699", "active": "#66cc80"}
RED = {"idle": "#e2979c", "hover": "#db8086", "active": "#d26067"}
FONT_NAME = "Chalkduster"
DEFAULT_BACKGROUND = "gainsboro"


def style_button(button, color):
    """
    formats each given button to have the same style
    :param button: the button to format
    :param color: the color of the button
    """
    button.configure(
        font=(FONT_NAME, 18, "bold"),
        width=500,
        height=50,
        borderless=True,
        bg="white",
        fg=color["idle"],
        overforeground="white",
        overbackground=color["hover"],
        activebackground=color["active"],
        focuscolor="",
    )


class QuizUI:
    """
    The GUI for the flashcard program
    """
    def __init__(self, quiz):
        """
        sets up the GUI window and starts the main loop
        :param quiz: the bank of questions
        """

        self.quiz = quiz

        # load in the UI sounds
        pygame.mixer.init()
        self.correct_sound = pygame.mixer.Sound("Audio/correct.wav")
        self.incorrect_sound = pygame.mixer.Sound("Audio/incorrect.wav")

        # create a window
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=50, pady=100, background=DEFAULT_BACKGROUND)

        # create a label to display user's current score
        self.score_label = Label(font=(FONT_NAME, 35, "normal"), background=DEFAULT_BACKGROUND)
        self.score_label.grid(column=1, row=0)

        # create a label to display the question
        self.question_label = Label(wraplength=600, height=18, width=50, font=(FONT_NAME, 24, "normal"))
        self.question_label.config()
        self.question_label.grid(column=1, row=1)

        # true button
        self.true_button = tkmacosx.Button(text="True", command=self.true_button_clicked)
        style_button(self.true_button, GREEN)
        self.true_button.grid(column=1, row=2)

        # false button
        self.false_button = tkmacosx.Button(text="False", command=self.false_button_clicked)
        style_button(self.false_button, RED)
        self.false_button.grid(column=1, row=3)

        # start the question tally at 0
        self.questions_right = 0
        self.questions_completed = 0

        self.question = None
        self.update_question()  # load in the first question
        self.window.mainloop()  # main loop

    def update_question(self):
        """
        Loads in the next question from the quiz and updates the labels.
        """
        self.score_label["text"] = f"{self.questions_right}/{self.questions_completed}"
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.question_label["text"] = f"Question #{self.quiz.question_number}\n\n\n{self.question.text}"
            self.questions_completed += 1
        else:
            self.question_label["text"] = "Thanks for playing!"
            self.true_button.destroy()
            self.false_button.destroy()

    def true_button_clicked(self):
        """
        Event that is executed when the true button is clicked.
        Method determines if the user's answer is correct or incorrect.
        """
        if "True" == self.question.answer:
            self.correct()
        else:
            self.incorrect()
        self.update_question()

    def false_button_clicked(self):
        """
        Event that is executed when the false button is clicked.
        Method determines if the user's answer is correct or incorrect.
        """
        if "False" == self.question.answer:
            self.correct()
        else:
            self.incorrect()
        self.update_question()

    def correct(self):
        """
        Plays the correct sound and changes the background to green for 1sec.
        Updates the number of correct answers
        """
        pygame.mixer.Sound.play(self.correct_sound)
        self.questions_right += 1
        self.change_background(GREEN["idle"])
        self.window.after(1000, self.clear)

    def incorrect(self):
        """
        Plays the incorrect sound and changes the background to red for 1sec
        """
        pygame.mixer.Sound.play(self.incorrect_sound)
        self.change_background(RED["idle"])
        self.window.after(1000, self.clear)

    def clear(self):
        """
        Changes the background to gray
        """
        self.change_background(DEFAULT_BACKGROUND)

    def change_background(self, color):
        """
        Changes the background of the window to the selected color
        :param color: new color for background
        """
        self.window.config(bg=color)
        self.score_label.config(bg=color)
