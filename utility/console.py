import time

class Console:

    def __init__(self) -> None:
        # Lookin' at the Devil and the Angel on my shoulder.
        pass

    def clear(self, delay: int | float = 0, units: str = 'sec') -> None:
        units = units.lower()

        if units == 'sec':
            pass
        elif units == 'min':
            delay = delay * 60
        elif units == 'hours':
            delay = delay * 60 * 60
        elif units == 'days':
            delay = delay * 60 * 60 * 24
        elif units == 'miliseconds':
            delay = delay / 60
        else:
            pass

        time.sleep(delay)
        print("\033[H\033[3J", end = '')

    def color_text(self, text: str, r: int = 255, g: int = 255, b: int = 255) -> str:
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"
