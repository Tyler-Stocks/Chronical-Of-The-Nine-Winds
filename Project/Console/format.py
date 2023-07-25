from time import sleep
from os import system
from shutil import get_terminal_size

def clear_console(
    delay: float = 0.0
    ) -> None:
    sleep(delay)
    system('cls')

def color_text(
    text:  str,
    red:   int = 255,
    green: int = 255,
    blue:  int = 255,
    ) -> str:
    return f'\033[38;2;{red};{green};{blue}m{text}\033[0m'

def center_text(
    text: str
    ) -> str:
    return ''.join([line.center(get_terminal_size().columns) for line in text.splitlines()])

def blink_text(
    text: str
    ) -> str:
    return f'\033[5m] {text} \033[5m'