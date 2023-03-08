class base_stats:

    def __init__(self):
        self.base_stats_list = [
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

        return self.base_stats_list

    def add(self, key, value):

        for stat_dict in self.base_stats_list:

            if key in stat_dict:
                current_value = stat_dict[key]
                stat_dict[key] = current_value + value
                break

        else:

            print(f'The key {key} was not found in the dictionary, please check your spelling, or add the key to the dictionary.')

    def edit(self, key, value):

        for stat_dict in self.base_stats_list:

            if key in stat_dict:

                stat_dict[key] = value
                break

        else:

            print(f'The key {key} was not found in the dictionary, please check your spelling, or add the key to the dictionary.')
