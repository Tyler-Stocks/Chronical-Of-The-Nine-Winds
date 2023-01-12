"""This is interesting lol"""
class Currency:
    """Class representing a currency in the game"""
    def __init__(self, name, amount):
        """Initialize a new currency instance with a name and an amount"""
        self.name = name
        self.amount = amount
    def add_amount(self, value):
        """Add a value to the current amount of the currency"""
        self.amount += value
