class BaseStats:

    def __init__(self):

        self.base_stats= [
            {'Health': 500},
            {'Defense': 50},
            {'Magic Defense': 5},
            {'Mana': 2},
            {'Casting': 1},
            {'Arcane': 0},
            {'Charisma': 1},
            {'Agility': 2},
            {'Stealth': 3},
            {'Determination': 0},
            {'Intelect': 5},
        ]


    # To call this function use stats.add({Stat}, {Value})
    def add(self, key, value) -> list:

        for stat_dict in self.base_stats:

            if key in stat_dict:
                current_value = stat_dict[key]
                stat_dict[key] = current_value + value
                break

            else:
                print(f'The key {key} was not found in the dictionary, please check your spelling, or add the key to the dictionary.')

        return self.base_stats

    # To call this function use stats.edit({Stat}, {Value})
    def edit(self, key, value) -> list:

        for stat_dict in self.base_stats:

            if key in stat_dict:
                stat_dict[key] = value
                break

            else:
                print(f'The key {key} was not found in the dictionary, please check your spelling, or add the key to the dictionary.')

        return self.base_stats
