class Faction:
    def __init__(self, name, relation):
        self.name = name
        self.relation = relation

    def change_relation(self, new_relation):
        self.relation = new_relation
class FactionsList:
    def __init__(self):
        self.factions = [
            Faction('Guild of Explorers', 'Neutral'),
            Faction('Lamia', 'Neutral'),
            Faction('High Imperial Army', 'Neutral'),
            Faction('Court of the High Moon', 'Neutral'),
            Faction('Pirates', 'Neutral'),
            Faction('Thieves', 'Neutral'),
            Faction('Elemental', 'Neutral'),
            Faction('Spirit', 'Hostile'),
            Faction('Orc', 'Hostile'),
            Faction('Beast', 'Hostile'),
            Faction('High Elves', 'Friendly'),
            Faction('Iron Stone Dwarfs', 'Hostile'),
        ]
    def get_factions(self):
        return self.factions
    def find_faction(self,name):
        for faction in self.factions:
            if faction.name == name:
                return faction
    def change_faction_relation(self,name,new_relation):
        faction = self.find_faction(name)
        if faction:
            faction.change_relation(new_relation)
            return True
    def change_all_relations(self, new_relation):
        for faction in self.factions:
            faction.change_relation(new_relation)