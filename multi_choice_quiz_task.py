from tkinter import *


class Quiz:
    def __init__(self, window):
        question = Label(window, text="Question:\t\tWhat are the first 10 digits of pi")
        choice_1 = Radiobutton(window, varaible="", value="", text="")

        question.grid(row=0, column=0)


root = Tk()
multi_choice_quiz = Quiz(root)
root.mainloop()
