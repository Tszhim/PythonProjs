import time
from tkinter import *
from question_bank_generator import QuestionBankGenerator
from trivia_info_manager import TriviaInfoManager

theme_color = "#375362"


class TriviaInterface:

    def __init__(self):

        # Initializing question bank and information manager.
        self.question_bank_generator = QuestionBankGenerator()
        self.trivia_info_manager = TriviaInfoManager(self.question_bank_generator.question_bank)

        # Setting up window.
        self.window = Tk()
        self.window.title("Trivia")
        self.window.config(padx=20, pady=20, bg=theme_color)

        # Setting up score label.
        self.score_label = Label(text="Score: 0/10", font=("Helvetica", 10, "normal"), fg="white", bg=theme_color)

        # Setting up canvas.
        self.canvas = Canvas(width=300, height=250, bg="White", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Press any button to start.",
                                                     font=("Helvetica", 12, "normal"), fill="black")
        self.title_screen = True

        # Setting up true and false buttons.
        true_button_img = PhotoImage(file="./images/true.png")
        false_button_img = PhotoImage(file="./images/false.png")
        self.true_button = Button(bg=theme_color, image=true_button_img, command=self.selected_true)
        self.false_button = Button(bg=theme_color, image=false_button_img, command=self.selected_false)

        # Positioning widgets via grid.
        self.score_label.grid(row=0, column=1, padx=10, pady=10)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=30)
        self.true_button.grid(row=2, column=0, pady=20)
        self.false_button.grid(row=2, column=1, pady=20)

        self.window.mainloop()

    # Button command if player responds "true".
    def selected_true(self) -> None:
        self.screen_update("True")

    # Button command if player responds "false".
    def selected_false(self) -> None:
        self.screen_update("False")

    # Updates window after each question.
    def screen_update(self, selection):

        # If on the title screen, only update the screen such that it shows the first question.
        if self.title_screen:
            self.trivia_info_manager.next_question()
            self.score_label.config(text="Score: " + str(self.trivia_info_manager.player_score) + "/10")
            self.canvas.itemconfig(self.question_text, text=self.trivia_info_manager.current_screen_text)
            self.title_screen = False

        # If not on the title screen and the question bank isn't empty, update the screen such that it shows the next question.
        elif not self.trivia_info_manager.bank_empty():
            self.check_correct(selection)
            self.trivia_info_manager.next_question()
            self.score_label.config(text="Score: " + str(self.trivia_info_manager.player_score) + "/10")
            self.canvas.itemconfig(self.question_text, text=self.trivia_info_manager.current_screen_text)

        # If the player has finished the trivia game.
        else:
            self.check_correct(selection)
            self.score_label.config(text="Score: " + str(self.trivia_info_manager.player_score) + "/10")
            self.trivia_finish()

    # Checks correctness and flashes red or green accordingly.
    def check_correct(self, selection):
        is_correct = self.trivia_info_manager.correct(selection)
        if is_correct:
            self.canvas.config(bg="green")
            self.canvas.update()
            time.sleep(1)
        else:
            self.canvas.config(bg="red")
            self.canvas.update()
            time.sleep(1)
        self.canvas.config(bg="white")

    # Showing end screen text after player has finished.
    def trivia_finish(self) -> None:
        # Disabling buttons.
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        # Updating screen text.
        if 0 <= self.trivia_info_manager.player_score <= 3:
            self.canvas.itemconfig(self.question_text, text="Better luck next time, study up more!")
        elif 4 <= self.trivia_info_manager.player_score <= 6:
            self.canvas.itemconfig(self.question_text, text="Good effort, but there is still\nroom for improvement!")
        elif 7 <= self.trivia_info_manager.player_score <= 9:
            self.canvas.itemconfig(self.question_text, text="Very well done, almost perfect!")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the pinnacle of skill!")
