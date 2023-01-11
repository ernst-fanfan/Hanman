import json
import random

"""This module manages and processes the words list."""


class WordsManager:
    words_dict: dict

    def __init__(self, file_name: str = './word_dictionary_module/dictionary.json'):
        with open(file_name, 'r') as open_file:
            self.words_dict = json.load(open_file)

    def random_word(self) -> str:
        return random.choice(self.words_dict["words"])


