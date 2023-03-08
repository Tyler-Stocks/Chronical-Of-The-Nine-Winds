class Player_Inventory():

    def __init__(self):
        self.inventory = []

    # This function is called as follows Player_Inventory.add('Item')
    def add(self, item):

        self.inventory.append(item)

    # This function is called as follows: Player_Inventory.remove('Item')
    def remove(self, item):

        self.inventory.append(item)

    # This function is called as follows Player_Inventory.display()
    def display(self):

        print(self.inventory)

    # This function is called as follows Player_Inventory.check()
    def check(self):

        inventory_item_amount = len(self.inventory)

        print(f'The amount of items in your inventory are {inventory_item_amount}.')