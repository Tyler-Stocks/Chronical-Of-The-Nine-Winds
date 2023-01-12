"""
Class to keep track of the items in an inventory.
"""
class Inventory:
    """
    Class to keep track of the items in an inventory.
    """
    def __init__(self):
        """
        Initialize an empty dictionary to store the items in the inventory.
        """
        self.items = {}

    def add(self, item, qty):
        """
        Add an item to the inventory.
        :param item: Name of the item to be added.
        :param qty: Quantity of the item to be added.
        """
        self.items[item] = self.items.get(item, 0) + qty

    def remove(self, item, qty):
        """
        Remove an item from the inventory.
        :param item: Name of the item to be removed.
        :param qty: Quantity of the item to be removed.
        """
        if item in self.items:
            self.items[item] -= qty
            if self.items[item] <= 0:
                del self.items[item]

    def check(self):
        """
        Check the items in the inventory.
        :return: Dictionary containing the items in the inventory and their quantities.
        """
        return self.items
