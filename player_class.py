from factions import FactionsList
from base_stats import Player
from currency import Currency

# Creates an instance of the player
player = Player()
# Creates the currency for gold
gold = Currency('gold', 0)
# Creates an instance of all of the factions
factions = FactionsList()

class PlayerClass:
    def player_class(self):
        # Prints out the different options for the player class
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

        # Asks for the user input so that the progarm can know what class they are
        player_class_choice = int(input())

        # Handles if the user chooses the 'freelancer' class
        if player_class_choice == 1:
            # Changes the starting money
            gold.add_amount(300)
            # Changes the relationship to the different factions, this will later affect what in game decisions can be made
            factions.change_all_relations('Friendly')
            # Lets the user know that they have choosen the class
            print("\nYou have choosen the Freelancer class.\n")
            # Handles if the user chooses the 'explorer' class
        elif player_class_choice == 2:
            # Changes the starting money
            gold.add_amount(200)
            # Changes the relationship to the different factions, this will later affect what in game decisions can be made
            factions.change_faction_relation('Lamia', 'Hostile')
            factions.change_faction_relation('Guild of Explorers', 'Friendly')
            # Changes the stats of the character
            player.change_stat('Perception', 15)
            # Lets the user know that they have choosen the class
            print("\nYou have choosen the Explorer class.\n")
        # Handles if the user chooses the 'knight of the imperial high throne' class
        elif player_class_choice == 3:
            # Changes the starting gold
            gold.add_amount(500)
            # Changes the relationship to the different factions, this will later affect what in game decisions can be made
            factions.change_faction_relation('High Imperial Army', 'Friendly')
            factions.change_faction_relation('Court of the Hight Moon', 'Friendly')
            factions.change_faction_relation('Pirates', 'Hostile')
            factions.change_faction_relation('Thieves', 'Hostile')
            # Changes the stats of the character
            player.change_stat('Strength', 50)
            # Lets the user know that they have choosen the class
            print("\nYou have choosen the Knight class.\n")
        # Handles if the user chooses the 'sage' class
        elif player_class_choice == 4:
            # Changes the relationship to the different factions, this will later affect what in game decisions can be made
            factions.change_all_relations('Ignored')
            # Changes the stats of the characters
            player.change_stat('Magic', 500)
            # Lets the user know that they have choosen the class
            print("You have choosen the Sage class.")
        # Handles if the user chooses the 'blind prophet' class
        elif player_class_choice == 5:
            # Changes the relationship to the different factions, this will later affect what in game decisios can be made
            factions.change_all_relations('Ignored')
            # Changes the stats of the character
            player.change_stat('Ambush Chance', 20)
            # Sets the isClass variable to true
            print('You have choosen the Blind Prophet class.')
        # Handles if the user inputs something incorrectly
        else:
            print("It appears that you have inputed something wrong, please try again.")