from tkinter import *


class Interface:
    def __init__(self, window):
        self.v = StringVar()
        self.v.set(None)
        self.q = Quiz()
        label1 = Label(window, text="Question:")
        question = Label(window, text=self.q.question)
        for i in range(len(self.q.answers)):
            Radiobutton(window, variable=self.v, value=self.q.answers[i], command=self.checker, text=self.q.answers[i])\
                .grid(row=i + 1, column=1)
        label1.grid(row=0, column=0)
        question.grid(row=0, column=1)

        self.label2 = Label(window, text="Please select an answer")
        self.label2.grid(row=90, columnspan=2, column=0)

    def checker(self):
        t = self.q.check_answer(self.v.get())
        self.label2.configure(text=t)


class Quiz:
    def __init__(self):
        self.question = "What is the most common last name in the world?"
        self.answers = ["Zhang", "Li", "Wang", "Chen"]
        self.display_answer = "Please select a choice"

    def check_answer(self, answer):
        if answer == "Wang":
            return "Correct!"
        else:
            return "Incorrect!"


root = Tk()
interface = Interface(root)
user_answer = interface.v
checking = Quiz()
root.mainloop()
