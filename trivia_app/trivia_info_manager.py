import html
from typing import List

from question_format import Question


class TriviaInfoManager:

    # Setting default instance values.
    def __init__(self, question_bank: List[Question]):
        self.player_score = 0
        self.question_bank_index = 0
        self.question_bank = question_bank
        for question in question_bank:
            print(question.question_text)
            print(question.answer_text)

        self.current_question = None
        self.current_screen_text = ""

    # Returns true if question bank is empty, false otherwise.
    def bank_empty(self) -> bool:
        if self.question_bank_index < len(self.question_bank):
            return False
        else:
            return True

    # Pushes current question index forward by 1.
    def next_question(self) -> None:
        self.current_question = self.question_bank[self.question_bank_index]
        self.question_bank_index = self.question_bank_index + 1
        self.format_screen_text()

    # Returns true if player answer is correct, false otherwise.
    def correct(self, boolean: str) -> bool:
        if boolean == self.current_question.answer_text:
            self.player_score = self.player_score + 1
            return True
        else:
            return False

    # Formats question text on screen such that it does not overflow out of the window.
    def format_screen_text(self) -> None:
        raw_string = html.unescape(self.current_question.question_text)
        output_string = ""
        last_space_index = 0
        last_new_line_index = [0]

        for i in range(0, len(raw_string)):

            # Attempts to find opportunity to new line such that it does not interject in the middle of a word.
            if i - last_new_line_index[-1] > 20 and raw_string[i] == " ":
                output_string = output_string + raw_string[last_new_line_index[-1]:i] + "\n"
                last_new_line_index.append(i + 1)
                last_space_index = 0

            # If the word is exceedingly long (15 letters+), new line and add hyphen.
            elif i - last_new_line_index[-1] > 20 and last_space_index > 15:
                output_string = output_string + raw_string[last_new_line_index[-1]:i] + "\n" + "-"
                last_new_line_index.append(i + 1)
                last_space_index = 0

            # Tracking last space found.
            elif raw_string[i] == " ":
                last_space_index = 0

            # Incrementing space index if space not found.
            else:
                last_space_index = last_space_index + 1

        # Adding final substring.
        if last_new_line_index[-1] != len(raw_string):
            output_string = output_string + raw_string[last_new_line_index[-1]:len(raw_string)]

        # Numbering question.
        self.current_screen_text = str(self.question_bank_index) + ") " + output_string
