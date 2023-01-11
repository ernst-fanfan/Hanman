"""This test module tests the words_manager_module."""

from word_dictionary_module.words_manager import WordsManager


class Test_Words_Manager_Module:
    words_manager = WordsManager()

    def test_words_dict(self):
        """Test if json file loaded."""
        assert self.words_manager.words_dict is not None
        assert self.words_manager.words_dict['name'] == "dictionary"
        assert type(self.words_manager.words_dict['words']) == list
        assert len(self.words_manager.words_dict['words']) > 100

    def test_random_word(self):
        """Test random_word function."""
        rand_word = self.words_manager.random_word()
        assert rand_word in self.words_manager.words_dict['words']
        assert len(rand_word) > 3
