from factions import FactionsList
from base_stats import Player
from currency import Currency

player = Player()
gold = Currency('gold', 0)
factions = FactionsList()

class PlayerClass:
    def player_class(self):
        print("""What class are you:
            1. Freelancer:
                You were born into a completely average family, growing up in an ordinary job, and thus having no special experience. As a consequence of you completely mediocre
                birth conditions you are neither loved nor hated, by all amicable factions. Finally, your parents being neither rich nor poor, gave you a decent amount of money
                to put into the bank.
                Starting Gold: 500
                Favour: All: Neutral
            2. Explorer:
                You were born to a guild of explorers. You have drifted from place to place all of you life, never staying in one place for long. As such your perceptions, and
                agility are much increased. Due to your assoiation with the guild, those of similar mindset will welcome you more easily. However, the guild has enemies,
                and should you find yourself in the hands of the Lamia, you will not be so fortunate as others. Finally, the guild gave you a small starting fund to aid you on your
                expedition to unkown lands.
                Starting Gold: 200
                + 5 Perception
                + 10 Agility
                Relations: Guild of Explorers: Friendly
                Favour: Lamia: Hostile
            3. Knight:
                You were born in to a family of Imperial Knights. You underwent severe martial training from a very young age. As a consequence of this you have much more
                strength, and stamina than the average person. However, due to your association with the crown those of criminal mind will despise you. Finally, you have managed to
                save up your meager wage over the last 10 years to amount to a decent amount.
                Starting Gold: 350
                + 50 Stamina
                + 10 Attack
                Relations: High Imperial Army: Friendly
                Relations: Court Of The Hight Moon: Friendly
                Realtions: Pirates: Hostile
                Relations: Theives: Hostile
            4. Sage:
                You were born as one of the few who has a special proclivity for magic, as such you were taken away from you family, and inducted into the Court of the High Moon at
                a young age. After many years of vigiours training you intelect, and magical capabilities are stronger than ever. However, many fear you presence, and you will be
                ignored by all factions. The Court lacks funding, and as such gave you only a meager starting wage which you have been able to save up over the years.
                Starting Gold: 100
                +500 magic
                Relations: All: Ignored
            5. Blind Prophet:
                You were born blind, unable to see the world around you, as such your other senses have been heightend to compensate. As a result of this your chance of being
                ambushed is greatly reduced. You were cast out of your home at a young age, and as such you have no money saved up.
                -10 ambush chance.
                Relations: All: Neutral
    """)

        player_class_choice = int(input())

        if player_class_choice == 1:
            gold.add_amount(300)
            factions.change_all_relations('Friendly')
            print("\nYou have choosen the Freelancer class.\n")
        elif player_class_choice == 2:
            gold.add_amount(200)
            factions.change_faction_relation('Lamia', 'Hostile')
            factions.change_faction_relation('Guild of Explorers', 'Friendly')
            player.change_stat('Perception', 15)
            print("\nYou have choosen the Explorer class.\n")
        elif player_class_choice == 3:
            gold.add_amount(500)
            factions.change_faction_relation('High Imperial Army', 'Friendly')
            factions.change_faction_relation('Court of the Hight Moon', 'Friendly')
            factions.change_faction_relation('Pirates', 'Hostile')
            factions.change_faction_relation('Thieves', 'Hostile')
            player.change_stat('Strength', 50)
            print("\nYou have choosen the Knight class.\n")
        elif player_class_choice == 4:
            factions.change_all_relations('Ignored')
            player.change_stat('Magic', 500)
            print("You have choosen the Sage class.")
        elif player_class_choice == 5:
            factions.change_all_relations('Ignored')
            player.change_stat('Ambush Chance', 20)
            print('\nYou have choosen the Blind Prophet class.\n')
        else:
            print("\nIt appears that you have inputed something wrong, please try again.\n")