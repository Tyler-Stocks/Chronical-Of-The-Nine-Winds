def gameDifficulty():
    # Asks user to confirm difficulty for the game
    while True:
        difficulty = input("Please select your difficulty level Easy or Hard: ")
        difficultyConfirm = input("\nAre you sure?")
        if difficultyConfirm.lower() == "yes" or difficultyConfirm.lower() == "y":
            break
    return difficulty
