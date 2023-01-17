# pylint: disable=line-too-long
from inventory import Inventory


my_inventory = Inventory()
def tavern():
    """This also has to be here lol"""
    print("""You wake up in a small dimly lit room. To your right there is a small boy, he appears to be sleeping peacfully. To your left there is a door, it appears to be
             broken, and worn out.
         """)
    wake_up = input("""As you make to get up, you fell a wave of exhaustion roll over you. Will you:
                       A: Overcome the Exhaustion
                       B: Succumb to the Exhaustion
                """)
    if wake_up.lower() == "a":
        print("""You managed to overcome the exhaustion, as you get up you decide to look out the window. As you look north the clouds can be dimly seen as remote grey
                 shapes rolling over the hills. As you look down, you see a sprawling kinddom. Strangly enough, however, there is not a person in sight.
        """)
        take_bag = str(input("""As you look back to the room you see a bag of equipment, would you like to take the bag?
                            """))
        if take_bag.lower() == "yes":
            print("""You decide to take the bag, as you look inside hoping to find something interesting, you are dissapointed as there is nothing inside.
            """)
            my_inventory.add("Leather Bag", 1)
            inspect_workbench = input("As you look around you, you see an assortment of items on a workbench next to the boys bed. Would you like to inspect the workbench?")
        elif take_bag.lower() == "no":
            print("You decided to not take the bag, fair enough")
            inspect_workbench = input("As you look around you, you see an assortment of items on a workbench next to the boys bed. Would you like to inspect the workbench?")
    elif wake_up.lower() == "b":
        print("""Unable to overcome the exhaustion you fall back into slumber. You stray out of thought, and mind where each day is a life age of the earth.
                 Suddenly you are awoken by the small child. 'Wake up, wake up!', he cried. 'You must hurry, the master of the tavern requests to speak with you, although
                 if I were you I might want to bring you bag, things might get ugly.
        """)
        take_bag = str(input("Would you like to take the bag on your bedside table, as the boy suggests?"))
    else:
        
