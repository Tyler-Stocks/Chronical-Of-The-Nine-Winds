
class main():
    def main(self):
        print("As you walk out in to the street you are forced to wince as a large cloud obscures your vision. As you look around you see that you appear to be in a")
        print("small market place. One stand in particular catches your eye as you see a large assortment of mechanical items on the table.")
        inspect_market_bench = str(input("Would you like to go over to the bench."))
        if inspect_market_bench.lower() == "yes":
            print("You decided to go over to the bench, there is no one guarding it.")
            print("However, there is a small sign hanging over it that states:")
            print("Do not steal, or you will never forget.")
            steal_from_market_bench = str(input("Would you like to steal the mechanical diet."))
            if steal_from_market_bench.lower() == "yes":
                print("You decided to take one of the mechanical orbs, as you quickly walk away you feel a sharp pain in your chest.")
                print("As you look down you see a metal knife through your chest, as you collapse on the ground you see a pair of purple eyes looking down on you.")
                print("""-------------------------------------------------------------------------------------------------------------------------
                         |                                              You Died, theft is bad.                                                  |
                         |                                            You did not make it very far                                               |
                         |                                                  Cause of death:                                                      |
                         |                                                    Stupidity                                                          |
                         |                                                                                                                       |
                         -------------------------------------------------------------------------------------------------------------------------
                """)
