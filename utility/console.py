import time as t

class Console:

    def __init__(self) -> None:
        self.clear_screen = '\033[H\033[J'

    def clear(self, delay: int | float = 0) -> None:
        t.sleep(delay)
        print(self.clear_screen, end = '')