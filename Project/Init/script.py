from Project.Init.enable_color import enable_color
from Project.Init.fullscreen import full_screen
from Project.Init.create_files import create_data_folders

def Initilize() -> None:
    create_data_folders()
    enable_color()
    full_screen()