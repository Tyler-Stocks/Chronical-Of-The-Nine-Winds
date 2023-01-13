class Game:
    def __init__(self):
        self.difficulty = None

    def set_difficulty(self):
        while True:
            self.difficulty = input("Please select your difficulty level Easy or Hard: ")
            difficulty_confirm = input("\nAre you sure?")
            if difficulty_confirm.lower() == "yes" or difficulty_confirm.lower() == "y":
                break