from time import sleep
from os import system
from shutil import get_terminal_size

def clearConsole(delay: float = 0.0) -> None:
    sleep(delay)
    system('cls')

def colorText(text: str, r: int = 255, g: int = 255, b: int = 255) -> str:
    return f'\033[38;2;{r};{g};{b}m{text}\033[0m'

def centerText(text: str) -> str:
    return ''.join([line.center(get_terminal_size().columns) for line in text.splitlines()])

def blinkText(text: str) -> str:
    return f'\033[5m] {text} \033[5m'