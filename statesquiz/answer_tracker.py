import pandas

from review_sheet import ReviewSheet


class AnswerTracker:

    # Retrieving answers from .csv file and preparing player information.
    def __init__(self):
        self.answers = []
        self.data = pandas.read_csv("50_states.csv")
        self.states = self.data["state"].tolist()
        self.user_score = 0

    # Checks validity of player answer. If valid, increase score by 1.
    def valid_answer(self, user_input, screen, answer_checker):
        # If player prematurely exits the game, prepare review sheet for them.
        if user_input == "exit":
            review_sheet = ReviewSheet(answer_checker)
            review_sheet.prepare_review_sheet()
            screen.bye()

        # Removing case-sensitivity.
        user_input = user_input.lower()
        user_input = user_input.title()

        if user_input in self.states and user_input not in self.answers:
            self.user_score = self.user_score + 1
            self.answers.append(user_input)
            return True
        else:
            return False

    # Checks if player has completed the game.
    def completed_quiz(self):
        return len(self.answers) == 50
