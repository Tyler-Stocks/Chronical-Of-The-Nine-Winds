"""I have to put this here lol"""
from currency import currency_list

def add_currency(name, amount):
    """Cycles through"""
    for curr in currency_list():
        if curr['name'] == name:
            curr['amount'] = amount
            return
