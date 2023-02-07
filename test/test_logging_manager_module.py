"""This test module tests the log_manager_module."""

from log_module.log_manager import with_logging, erase_logs, read_log, debug
from random import randint
import pytest


@with_logging
def divider(num1: int, num2: int):
    return num1 / num2


class TestLogManagerModule:
    @pytest.mark.parametrize('param1, param2', [(1, 1), (10, 2),
                                                (randint(1, 100), randint(1, 100))])
    def test_with_logging_no_error(self, param1: int, param2: int, caplog):
        answer = divider(param1, param2)

        assert answer is not None
        assert len(caplog.records) == 2
        for record in caplog.records:
            assert record.levelname == 'INFO'

        assert 'divider' in caplog.text
        assert 'HANGMAN' in caplog.text
        assert caplog.text.count('divider') == 2
        assert caplog.text.count('HANGMAN') == 2

    @pytest.mark.parametrize('param1, param2', [(1, 0), (10, 0),
                                                (randint(1, 100), 0)])
    def test_with_logging_with_error(self, param1: int, param2: int, caplog):
        answer = divider(param1, param2)

        assert answer is None
        assert len(caplog.records) == 3
        assert 'divider' in caplog.text
        assert 'HANGMAN' in caplog.text
        assert caplog.text.count('divider') == 3
        assert caplog.text.count('HANGMAN') == 3
        assert caplog.records[0].levelname == 'INFO'
        assert caplog.records[1].levelname == 'DEBUG'
        assert caplog.records[2].levelname == 'INFO'


