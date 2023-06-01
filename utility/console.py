"""
The 'console' module allows for you to interact with the console in different ways.
Structure:
Console
|
|--__init__(self) -> None
|
|--clear(self, delay(int | float) = 0) -> None
|
|--color_test(self, text(str), color(str) = 'white', bold(bool) = False) -> str
"""

import time

class Console:
    """Different Functions for interacting with the console"""

    def __init__(self) -> None:
        self.escape_sequence = '\033[{}m'
        self.colors = {
            'black': 30,
            'red': 31,
            'green': 32,
            'yellow': 33,
            'blue': 34,
            'magenta': 35,
            'cyan': 36,
            'white': 37
            }

    def clear(self, delay: int | float = 0 ) -> None:
        """
        Clears Console after delay.

        Args:
            delay (int): The delay before clearing the console
        """
        time.sleep(delay)
        print('\033[H\033[J', end='')

    def color_text(self, text: str, color: str = 'white', bold: bool = False) -> str:
        """
        Colorizes the given text using ANSI escape sequences.

        Args:
            text (str): The text to colorize.
            color (str): The desired text color. Default is 'white'.
            bold (bool): Whether to make the text bold. Default is False.

        Returns:
            str: The colorized text.
        """
        color_code = self.colors.get(color.lower(), 37)
        if bold:
            color_code = f'1;{color_code}'

        return self.escape_sequence.format(color_code) + text + self.escape_sequence.format(0)
