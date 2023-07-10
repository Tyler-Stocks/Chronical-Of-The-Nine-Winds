import time
import os

class Console:

    def __init__(self):
        pass

    def clear(self, delay: int | float = 0) -> None:
        time.sleep(delay)
        os.system('cls')

    def color(self, text: str, r: int = 255, g: int = 255, b: int = 255) -> str:
        return f'\033[38;2;{r};{g};{b}m{text}\033[0m'
