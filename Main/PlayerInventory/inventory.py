class PlayerInventory():

    def __init__(self) -> None:

        self.inventory = []


    # This function is called as follows Player_Inventory.add('Item')
    def add(self, item) -> list:

        self.inventory.append(item)

        return self.inventory

    # This function is called as follows: Player_Inventory.remove('Item')
    def remove(self, item) -> list:

        self.inventory.append(item)

        return self.inventory

    # This function is called as follows Player_Inventory.display()
    def display(self) -> list:

        print(self.inventory)

        return self.inventory

    # This function is called as follows Player_Inventory.check()
    def check(self) -> list:

        inventory_item_amount = len(self.inventory)

        print(f'The amount of items in your inventory are {inventory_item_amount}.')

        return self.inventory
