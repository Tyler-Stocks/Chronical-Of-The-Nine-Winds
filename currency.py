class Currency:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def add_amount(self, value):
        self.amount += value
