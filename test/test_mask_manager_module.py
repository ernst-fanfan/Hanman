""" THis test module tests the mask_manager_module"""

from word_dictionary_module.mask_manager import MaskManager
import pytest


class Test_Mask_Manager_Module:
    @pytest.mark.parametrize("word", ["kissing", "love", "deaf", "fear"])
    def test_mask_word(self, word):
        """Test MaskManager instantiates and produce mask."""
        masker = MaskManager(word)
        mask = masker.masked
        assert mask is not None
        assert len(mask) == len(word)

    @pytest.mark.parametrize("word", ["kissing", "love", "deaf", "fear"])
    def test_update_mask_found(self, word):
        """Test MaskManager updates mask with letter found."""
        masker = MaskManager(word)
        mask = masker.masked
        idx = 2
        letter = word[idx]
        found = masker.update_mask(letter)
        updated_mask = masker.masked
        letter_count = word.count(letter)
        star_count = updated_mask.count(letter)

        assert found == True
        assert len(mask) == len(updated_mask)
        assert len(mask) == len(word)
        assert letter_count == star_count

    @pytest.mark.parametrize("word", ["kissing", "love", "deaf", "fear"])
    def test_update_mask_not_found(self, word):
        """Test MaskManager updates mask with letter not found."""
        masker = MaskManager(word)
        mask = masker.masked
        letter = "1"
        found = masker.update_mask(letter)
        updated_mask = masker.masked
        letter_count = word.count(letter)
        star_count = updated_mask.count(letter)

        assert found == False
        assert len(mask) == len(updated_mask)
        assert len(mask) == len(word)
        assert letter_count == star_count

