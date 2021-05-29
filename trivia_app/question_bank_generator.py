from data_retriever import DataRetriever
import question_format


class QuestionBankGenerator:

    # Stores data received from DataRetriever() as question objects.
    def __init__(self):
        self.data_retriever = DataRetriever()
        self.question_bank = []
        for question_data in self.data_retriever.trivia_question_data:
            question = question_format.Question(question_data["question"],
                                                question_data["correct_answer"])
            self.question_bank.append(question)
