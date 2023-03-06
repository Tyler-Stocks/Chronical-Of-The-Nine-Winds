class Player_Inventory():

    def __init__(self):
        self.inventory = []

    def add_item_to_inventory(self, item):

        self.inventory.append(item)

    def remove_item_from_inventory(self, item):

        self.inventory.append(item)

    def display_inventory_items(self):

        print(self.inventory)

    def check_how_many_items_are_in_inventory(self):

        inventory_item_amount = len(self.inventory)

        print(f'The amount of items in your inventory are {inventory_item_amount}.')