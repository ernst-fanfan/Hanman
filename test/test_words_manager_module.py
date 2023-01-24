"""This test module tests the words_manager_module."""

from word_dictionary_module.words_manager import WordsManager
import pytest


class TestWordsManagerModule:
    words_manager = WordsManager()

    def test_words_dict(self):
        """Test if json file loaded."""
        assert self.words_manager.words_dict is not None
        assert self.words_manager.words_dict['name'] == "dictionary"
        assert type(self.words_manager.words_dict['words']) == list
        assert len(self.words_manager.words_dict['words']) > 100

    @pytest.mark.parametrize("number_of_tries", [1, 4, 3, 10])
    def test_random_word(self, number_of_tries):
        """Test random_word function."""
        for _ in range(number_of_tries):
            rand_word1 = self.words_manager.random_word()
            rand_word2 = self.words_manager.random_word()
            assert rand_word1 in self.words_manager.words_dict['words']
            assert len(rand_word1) > 3
            assert rand_word2 in self.words_manager.words_dict['words']
            assert len(rand_word2) > 3
            assert rand_word2 != rand_word1
