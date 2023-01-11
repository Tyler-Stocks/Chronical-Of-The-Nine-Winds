"""This module contains the code for the early game of the game"""
from game_difficulty import game_difficulty
from variables import varList
from user_info import userInfo
from player_class import player_class


def early_game():
    """All of the functions for the early game"""
    # Defines a list of all of the variables used for early game
    varList()

    # Asks the user for Difficulty Selection
    game_difficulty()

    #Asks the user to input their name, and age
    userInfo()

    # Asks user to choose a class, and then modifies their stats based on the choice
    player_class()
