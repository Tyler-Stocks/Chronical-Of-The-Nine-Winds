class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def attack(self, enemy):
        enemy.health -= 10
    def defend(self):
        self.health += 5
    def is_alive(self):
        return self.health > 0

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def attack(self, player):
        player.health -= 5
    def is_alive(self):
        return self.health > 0

def combat_loop(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f'{enemy.name} has {enemy.health} health')
        print(f'{player.name} has {player.health} health')
        print('What would you like to do?')
        print('1. Attack')
        print('2. Defend')
        action = input()
        if action == '1':
            player.attack(enemy)
        elif action == '2':
            player.defend()
        enemy.attack(player)
    if player.is_alive():
        print(f'{player.name} has defeated {enemy.name}!')
    else:
        print(f'{player.name} has been defeated by {enemy.name}.')

