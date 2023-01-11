"""This module manages the mask for the chosen word"""


class MaskManager:
    word: str
    masked: str

    def __init__(self, word: str) -> None:
        self.word = word
        self.mask_word()

    def mask_word(self) -> None:
        self.masked = '*' * len(self.word)

    def update_mask(self, letter: chr) -> bool:
        found = False
        word_as_list = list(self.word)
        print(word_as_list)
        for idx in range(len(word_as_list)):
            if word_as_list[idx] == letter:
                masked_as_list = list(self.masked)
                print(masked_as_list)
                masked_as_list[idx] = letter
                self.masked = ''.join(masked_as_list)
                found = True
        return found
