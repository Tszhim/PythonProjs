import pandas


class ReviewSheet:

    def __init__(self, answer_tracker):
        self.missed_states = []
        for state in answer_tracker.states:
            if state not in answer_tracker.answers:
                self.missed_states.append(state)

    def prepare_review_sheet(self):
        pandas.DataFrame(self.missed_states).to_csv("review_sheet.csv")
