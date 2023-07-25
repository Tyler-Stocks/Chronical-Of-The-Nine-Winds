from time import sleep
from os import system
from shutil import get_terminal_size

def clearConsole(
    delay: float = 0.0,
    ) -> None:
    sleep(delay)
    system('cls')

def colorText(
    text: str,
    red: int = 255,
    green: int = 255,
    blue: int = 255,
    ) -> str:
    return f'\033[38;2;{red};{green};{blue}m{text}\033[0m'

def centerText(
    text: str,
    ) -> str:
    return ''.join([line.center(get_terminal_size().columns) for line in text.splitlines()])

def blinkText(
    text: str,
    ) -> str:
    return f'\033[5m] {text} \033[5m'