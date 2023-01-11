"""Function to confirm the basics"""
def game_difficulty():
    """Confirms the difficulty"""
    # Asks user to confirm difficulty for the game
    while True:
        difficulty = input("Please select your difficulty level Easy or Hard: ")
        difficulty_confirm = input("\nAre you sure?")
        if difficulty_confirm.lower() == "yes" or difficulty_confirm.lower() == "y":
            break
    return difficulty
