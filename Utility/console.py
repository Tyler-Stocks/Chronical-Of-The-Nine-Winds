import time


class Console:

    def __init__(self):
        pass

    def clear(self, delay):
        time.sleep(delay)
        print('\033[H\033[J', end='')
