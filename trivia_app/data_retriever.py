import requests


class DataRetriever:

    # Retrieves question and answer data from opentdb api.
    def __init__(self):
        trivia_general = requests.get(url="https://opentdb.com/api.php", params={"amount": 10, "type": "boolean"})
        trivia_general.raise_for_status()
        trivia_general_data = trivia_general.json()
        self.trivia_question_data = trivia_general_data["results"]
