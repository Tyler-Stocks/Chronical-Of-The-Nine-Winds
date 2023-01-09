from gameDifficulty import gameDifficulty ; from variables import varList
from userInfo import userInfo ; from playerClass import playerClass


def EarlyGame():
    # Defines a list of all of the variables used for early game
    varList()

    # Asks the user for Difficulty Selection
    gameDifficulty()

    #Asks the user to input their name, and age
    userInfo()

    # Asks user to choose a class, and then modifies their stats, and attributes based on the class provided
    playerClass()
