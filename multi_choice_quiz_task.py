from tkinter import *


class Quiz:
    def __init__(self, window):
        f1 = Frame(window)
        f2 = Frame(window)
        f3 = Frame(window)
        answers = ["Zhang", "Li", "Wang", "Chen"]
        self.v = StringVar()
        self.v.set(None)
        label1 = Label(f1, text="Question:")
        question = Label(f2, text="What is the most common last name in the world?")
        for i in range(len(answers)):
            Radiobutton(f2, variable=self.v, value=answers[i], text=answers[i], command=self.right_or_wrong)\
                .grid(row=i+1, column=0)

        self.answer_display = Label(f3, text="Please select an answer")

        f1.grid(row=0, column=0, sticky=N)
        f2.grid(row=0, column=1)
        f3.grid(row=1, column=0, columnspan=2)
        label1.grid(row=0, column=0, sticky=N)
        question.grid(row=0, column=0)
        self.answer_display.grid(row=0, column=0)

    def right_or_wrong(self):
        if self.v.get() == "Wang":
            self.answer_display.configure(text="Correct!")
        else:
            self.answer_display.configure(text="Incorrect!")


root = Tk()
multi_choice_quiz = Quiz(root)
root.mainloop()
