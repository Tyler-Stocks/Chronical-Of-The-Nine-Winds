class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, item, qty):
        self.items[item] = self.items.get(item, 0) + qty

    def remove(self, item, qty):
        if item in self.items:
            self.items[item] -= qty
            if self.items[item] <= 0:
                del self.items[item]

    def check(self):
        return self.items
