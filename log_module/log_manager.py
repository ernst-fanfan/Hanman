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

# for testing purposes. will replace with a constant file
APP = 'HANGMAN'

# START OF SCRIPT
WrappedReturn = TypeVar("WrappedReturn")
WrappedParams = ParamSpec("WrappedParams")

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)
# TODO: erase after gae
logging.basicConfig(filename=f'{APP}.log',
                    format='%(asctime)s %(message)s',
                    filemode='w')


def parse_script_name(path):
    return os.path.basename(path)


def with_logging(func: Callable[WrappedParams, WrappedReturn]) -> Callable[
    WrappedParams, WrappedReturn]:
    name = parse_script_name(__file__)
    preamble = f"INFO|{APP}|{name}"

    @functools.wraps(func)
    def wrapper(*args: WrappedParams.args, **kwargs: WrappedParams.kwargs) -> WrappedReturn:
        logging.info(preamble + f": Calling {func.__name__}")
        value = None
        try:
            value = func(*args, **kwargs)
        except BaseException as error:
            logging.debug(preamble.replace('INFO', 'ERROR') + f"|{func.__name__}: {error}")

        logging.info(preamble + f": Finished {func.__name__}")
        return value

    return wrapper


def debug(message: str = "") -> None:
    name = parse_script_name(__file__)
    preamble = f"DEBUG|{APP}|{name}"
    logging.debug(msg=preamble + f": {message}")

