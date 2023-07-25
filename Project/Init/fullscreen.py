from win32gui import GetForegroundWindow, ShowWindow
from win32con import SW_MAXIMIZE

def full_screen() -> None:
    ShowWindow(GetForegroundWindow(), SW_MAXIMIZE)
