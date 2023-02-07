"""This test module tests the log_manager_module."""

from log_module.log_manager import with_logging, debug
from random import randint
import pytest


class TestLogManagerModule:
    d_filename: str = 'HANGMAN.log'

    @pytest.mark.parametrize('param1, param2', [(1, 1), (10, 2),
                                                (randint(1, 100), randint(1, 100))])
    def test_with_logging_no_error(self, param1: int, param2: int):
        @with_logging
        def divider(num1: int, num2: int):
            return num1 / num2

        answer = divider(param1, param2)
        assert answer is not None

        with open(self.d_filename, 'w') as file:
            imported_file = file.read()
            assert 'INFO' in imported_file
            assert imported_file.count("INFO") == 3
