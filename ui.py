from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="???",
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20, padx=20)

        self.score_text = Label(text="Score: 0", font=("Arial", 12, "normal"), fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        tick = PhotoImage(file="images/true.png")
        self.tick_button = Button(image=tick, bg=THEME_COLOR,
                                  highlightthickness=0,
                                  command=self.tick_clicked)
        self.tick_button.grid(row=2, column=0, padx=20, pady=20)

        cross = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross, bg=THEME_COLOR,
                                   highlightthickness=0,
                                   command=self.cross_clicked)
        self.cross_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz. \n"
                                                            f" Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def tick_clicked(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def cross_clicked(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
