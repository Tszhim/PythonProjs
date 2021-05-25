import pandas
import random

class WordGenerator:

    def __init__(self):
        try:
            words = pandas.read_csv("data/review_words.csv")
            self.cantonese_word_list = words["Cantonese"].to_list()
            self.english_word_list = words["English"].to_list()
        except FileNotFoundError:
            words = pandas.read_csv("data/cantonese_words.csv")
            self.cantonese_word_list = words["Cantonese"].to_list()
            self.english_word_list = words["English"].to_list()

    def random_word(self):
        index = random.randint(0, len(self.cantonese_word_list) - 1)
        return {"Cantonese": self.cantonese_word_list[index], "English": self.english_word_list[index]}

    def remove_word_pair(self, cantonese_word, english_word):
        self.cantonese_word_list.remove(cantonese_word)
        self.english_word_list.remove(english_word)
        review_words_dict = {
            "Cantonese": self.cantonese_word_list,
            "English": self.english_word_list
        }
        review_words = pandas.DataFrame(review_words_dict)
        review_words.to_csv("data/review_words.csv")




