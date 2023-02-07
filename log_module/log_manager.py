"""This module handles logging.
It contains the logging wrapper func def.
example of use:
    @with_logging
    def mtk():
        return 1 / 0
        ...
and a debugger function.
"""

import logging
import os
import functools
from typing import Callable, TypeVar, ParamSpec

APP = 'HANGMAN'
WrappedReturn = TypeVar("WrappedReturn")
WrappedParams = ParamSpec("WrappedParams")
filename = f'{APP}.log'
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename=filename,
                    format='%(asctime)s %(message)s',
                    filemode='a')


def parse_script_name(path):
    return os.path.basename(path)


def erase_logs() -> None:
    with open(filename, 'w') as file:
        file.write("")


def read_log() -> str:
    with open(filename, 'r') as file:
        debug(f"file= {file.readlines()}")
        return file.readlines()


def debug(message: str = "") -> None:
    name = parse_script_name(__file__)
    preamble = f"DEBUG|{APP}|{name}"
    logger.debug(msg=preamble + f": {message}")


def with_logging(func: Callable[WrappedParams, WrappedReturn]) -> Callable[WrappedParams, WrappedReturn]:
    name = parse_script_name(__file__)
    preamble = f"INFO|{APP}|{name}"

    @functools.wraps(func)
    def wrapper(*args: WrappedParams.args, **kwargs: WrappedParams.kwargs) -> WrappedReturn:
        logger.info(preamble + f": Calling {func.__name__}")
        value = None
        try:
            value = func(*args, **kwargs)
        except BaseException as error:
            logger.debug(preamble.replace('INFO', 'ERROR') + f"|{func.__name__}: {error}")

        logger.info(preamble + f": Finished {func.__name__}")
        return value

    return wrapper


@with_logging
def divider(num1: int, num2: int):
    print('rknrn')
    return num1 / num2


divider(1, 1)
divider(1, 0)
