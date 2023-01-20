# pylint: disable=line-too-long
from inventory import Inventory


my_inventory = Inventory()
class Tavern():
    def tavern(self):
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
                print("You decide to take the bag, as you look inside hoping to find something interesting, you are dissapointed as there is nothing inside.")
                print("You obtained the leather bag!")
                my_inventory.add("Leather Bag", 1)
                inspect_workbench = input("As you look around you, you see an assortment of items on a workbench next to the boys bed. Would you like to inspect the workbench?")
                if inspect_workbench.lower() == "yes":
                    print("""You decided to inspect the workbench. On the workbench you see the following items:
                             An old map
                             A rusted bell
                             A piece of rotting wood
                             An leather book
                         """)
                    work_bench_choice = str(input("""Would you like to:
                                                   A: Examine the map
                                                   B: Examine the bell
                                                   C: Examine the piece of rotting wood
                                                   D: Open the leather book
                                                """))
                    if work_bench_choice.lower() == "a":
                        print("You decided to inspect the map, it is too faded to dechiper. If only you had the right tools...")
                        take_faded_map = str(input("Would you like to take the map? "))
                        if take_faded_map.lower() == "yes":
                            print("You decided to take the map, hopefully it will come in handy later.")
                            my_inventory.add("Faded Map", 1)
                            work_bench_choice_two = str(input("""Would you like to:
                                                                 A: Examine the bell
                                                                 B: Examine the piece of rotting wood
                                                                 C: Open the leather book
                                                             """))
                            if work_bench_choice_two.lower() == "a":
                                print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                take_rusted_bell = str(input("Would you like to take the bell? "))
                                if take_rusted_bell.lower() == "yes":
                                    print("You decided to take the bell, perhaps you can repair it later.")
                                    my_inventory.add("rusted_bell", 1)
                                    work_bench_choice_three = str(input("""Would you like to:
                                                                           A: Examine the piece of rotting wood
                                                                           B: Open the leather book
                                                                  """))
                                    if work_bench_choice_three.lower() == "a":
                                        print("It appears that there is a rotting piece of wood on the table")
                                        take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                                    elif work_bench_choice_three.lower() == "b":
                                        print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                        open_arcane_journal = str(input("Would you like to open the journal."))
                                    else:
                                        print("!")
                                elif take_rusted_bell.lower() == "no":
                                    print("You decided not to take the bell, it was broken anyways.")
                                    work_bench_choice_three = str(input("""Would you like to:
                                                                           A: Examine the piece of rotting wood
                                                                           B: Open the leather book
                                                                  """))
                                    if work_bench_choice_three.lower() == "a":
                                        print("It appears that there is a rotting piece of wood on the table")
                                        take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                                    elif work_bench_choice_three.lower() == "b":
                                        print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                        open_arcane_journal = str(input("Would you like to open the journal."))
                                    else:
                                        print("!")
                                else:
                                    print("!")
                            elif work_bench_choice_two.lower() == "b":
                                print("It appears that there is a rotting piece of wood on the table")
                                take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                                if take_rotting_wood.lower() == "yes":
                                    print("You decided to take the rotting wood, I'm sure there is some use for it.")
                                    my_inventory.add("Rotting Wood", 1)
                                    work_bench_choice_three = str(input("""Would you like to:
                                                                           A: Examine the bell
                                                                           B: Open the leather book
                                                                  """))
                                    if work_bench_choice_three.lower() == "a":
                                        print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                        take_rusted_bell = str(input("Would you like to take the bell? "))
                                    elif work_bench_choice_three.lower() == "b":
                                        print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                        open_arcane_journal = str(input("Would you like to open the journal."))
                                elif take_rotting_wood.lower() == "no":
                                    print("You decided to not take the rotting wood, fair enough")
                                    work_bench_choice_three = str(input("""Would you like to:
                                                                           A: Examine the bell
                                                                           B: Open the leather book
                                                                  """))
                                    if work_bench_choice_three.lower() == "a":
                                        print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                        take_rusted_bell = str(input("Would you like to take the bell? "))
                                    elif work_bench_choice_three.lower() == "b":
                                        print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                        open_arcane_journal = str(input("Would you like to open the journal."))
                                    else:
                                        print("!")
                                else:
                                    print("!")
                            elif work_bench_choice_two.lower() == "c":
                                print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                open_arcane_journal = str(input("Would you like to open the journal."))
                            else:
                                print("!")
                        elif take_faded_map.lower() == "no":
                            print("You decided not to take the map, probably not important. Right?")
                            work_bench_choice_two = str(input("""Would you like to:
                                                                 A: Examine the bell
                                                                 B: Examine the piece of rotting wood
                                                                 C: Open the leather book
                                                             """))
                            if work_bench_choice_two.lower() == "a":
                                print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                take_rusted_bell = str(input("Would you like to take the bell? "))
                                if take_rusted_bell.lower() == "yes":
                                    print("You decided to take the bell, perhaps you can repair it later.")
                                    my_inventory.add("rusted_bell", 1)
                                    work_bench_choice_three = str(input("""Would you like to:
                                                                           A: Examine the piece of rotting wood
                                                                           B: Open the leather book
                                                                  """))
                                    if work_bench_choice_three.lower() == "a":
                                        print("It appears that there is a rotting piece of wood on the table")
                                        take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                                    elif work_bench_choice_three.lower() == "b":
                                        print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                        open_arcane_journal = str(input("Would you like to open the journal."))
                                    else:
                                        print("!")
                                elif take_rusted_bell.lower() == "no":
                                    print("You decided not to take the bell, it was broken anyways.")
                                    work_bench_choice_three = str(input("""Would you like to:
                                                                           A: Examine the piece of rotting wood
                                                                           B: Open the leather book
                                                                  """))
                                    if work_bench_choice_three.lower() == "a":
                                        print("It appears that there is a rotting piece of wood on the table")
                                        take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                                    elif work_bench_choice_three.lower() == "b":
                                        print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                        open_arcane_journal = str(input("Would you like to open the journal."))
                                    else:
                                        print("!")
                                else:
                                    print("!")
                            elif work_bench_choice_two.lower() == "b":
                                print("It appears that there is a rotting piece of wood on the table")
                                take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                                if take_rotting_wood.lower() == "yes":
                                    print("You decided to take the rotting wood, I'm sure there is some use for it.")
                                    my_inventory.add("Rotting Wood", 1)
                                    work_bench_choice_three = str(input("""Would you like to:
                                                                           A: Examine the bell
                                                                           B: Open the leather book
                                                                  """))
                                    if work_bench_choice_three.lower() == "a":
                                        print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                        take_rusted_bell = str(input("Would you like to take the bell? "))
                                    elif work_bench_choice_three.lower() == "b":
                                        print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                        open_arcane_journal = str(input("Would you like to open the journal."))
                                elif take_rotting_wood.lower() == "no":
                                    print("You decided to not take the rotting wood, fair enough")
                                    work_bench_choice_three = str(input("""Would you like to:
                                                                           A: Examine the bell
                                                                           B: Open the leather book
                                                                  """))
                                    if work_bench_choice_three.lower() == "a":
                                        print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                        take_rusted_bell = str(input("Would you like to take the bell? "))
                                    elif work_bench_choice_three.lower() == "b":
                                        print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                        open_arcane_journal = str(input("Would you like to open the journal."))
                                    else:
                                        print("!")
                                else:
                                    print("!")
                            elif work_bench_choice_two.lower() == "c":
                                print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                open_arcane_journal = str(input("Would you like to open the journal."))
                            else:
                                print("!")
                        else:
                            print("!")
                    elif work_bench_choice.lower() == "b":
                        print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                        take_rusted_bell = str(input("Would you like to take the bell? "))
                        if take_rusted_bell.lower() == "yes":
                            print("You decided to take the bell, perhaps you can repair it later.")
                            my_inventory.add("rusted_bell", 1)
                            work_bench_choice_two = str(input("""Would you like to:
                                                                 A: Examine the map
                                                                 B: Examine the piece of rotting wood
                                                                 C: Open the leather book
                                                        """))
                            if work_bench_choice_two.lower() == "a":
                                print("You decided to inspect the map, it is too faded to dechiper. If only you had the right tools...")
                                take_faded_map = str(input("Would you like to take the map? "))
                            elif work_bench_choice_two.lower() == "b":
                                print("It appears that there is a rotting piece of wood on the table")
                                take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                            elif work_bench_choice_two.lower() == "c":
                                 print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                 open_arcane_journal = str(input("Would you like to open the journal."))
                            else:
                                print("!")
                        elif take_rusted_bell.lower() == "no":
                            print("You decided not to take the bell, it was broken anyways.")
                            work_bench_choice_two = str(input("""Would you like to:
                                                                 A: Examine the map
                                                                 B: Examine the piece of rotting wood
                                                                 C: Open the leather book
                                                        """))
                            if work_bench_choice_two.lower() == "a":
                                print("You decided to inspect the map, it is too faded to dechiper. If only you had the right tools...")
                                take_faded_map = str(input("Would you like to take the map? "))
                            elif work_bench_choice_two.lower() == "b":
                                print("It appears that there is a rotting piece of wood on the table")
                                take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                            elif work_bench_choice_two.lower() == "c":
                                print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                open_arcane_journal = str(input("Would you like to open the journal."))
                            else:
                                print("!")
                        else:
                            print("!")
                    elif work_bench_choice.lower() == "c":
                        print("It appears that there is a rotting piece of wood on the table")
                        take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                        if take_rotting_wood.lower() == "yes":
                            print("You decided to take the rotting wood, I'm sure there is some use for it.")
                            my_inventory.add("Rotting Wood", 1)
                            work_bench_choice_two = str(input("""Would you like to:
                                                                 A: Examine the map
                                                                 B: Open the leather book
                                                                 C: Examine the bell
                                                        """))
                            if work_bench_choice_two.lower() == "a":
                                print("You decided to inspect the map, it is too faded to dechiper. If only you had the right tools...")
                                take_faded_map = str(input("Would you like to take the map? "))
                            elif work_bench_choice_two.lower() == "b":
                                print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                open_arcane_journal = str(input("Would you like to open the journal."))
                            elif work_bench_choice_two.lower() == "c":
                                print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                take_rusted_bell = str(input("Would you like to take the bell? "))
                            else:
                                print("!")
                        elif take_rotting_wood.lower() == "no":
                            print("You decided to not take the rotting wood, fair enough")
                            work_bench_choice_two = str(input("""Would you like to:
                                                                 A: Examine the map
                                                                 B: Open the leather book
                                                                 C: Examine the bell
                                                        """))
                            if work_bench_choice_two.lower() == "a":
                                print("You decided to inspect the map, it is too faded to dechiper. If only you had the right tools...")
                                take_faded_map = str(input("Would you like to take the map? "))
                            elif work_bench_choice_two.lower() == "b":
                                print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                                open_arcane_journal = str(input("Would you like to open the journal."))
                            elif work_bench_choice_two.lower() == "c":
                                print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                take_rusted_bell = str(input("Would you like to take the bell? "))
                            else:
                                print("!")
                        else:
                            print("!")
                    elif work_bench_choice.lower() == "d":
                        print("As you get closer to the book you notice the words ARCANE JOURNAL printed in violet letters near the top.")
                        open_arcane_journal = str(input("Would you like to open the journal."))
                        if open_arcane_journal.lower() == "yes":
                            print("You decided to look in the journal, after flipping through the faded pages you manage to make out the following passage:")
                            print("""
                                  I have just finally been accepted into the brotherhood! It has been three months since I sent my application, I was starting to worry
                                  that I wouldn't get in. I am leaving tomorrow for the high imperial court. I can't wait to finally see the city, I heard the
                                  capital has near 10,000 people in it. So many people, I am sure it will be wonderfull.
                                 """)
                            my_inventory.add("Arcane Journal Entry One", 1)
                            work_bench_choice_two = str(input("""Would you like to:
                                                                 A: Examine the map
                                                                 B: Examine the bell
                                                                 C: Examine the rotting piece of wood
                                                             """))
                            if work_bench_choice_two.lower() == "a":
                                print("You decided to inspect the map, it is too faded to dechiper. If only you had the right tools...")
                                take_faded_map = str(input("Would you like to take the map? "))
                            elif work_bench_choice_two.lower() == "b":
                                print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                take_rusted_bell = str(input("Would you like to take the bell? "))
                            elif work_bench_choice_two.lower() == "c":
                                print("It appears that there is a rotting piece of wood on the table")
                                take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                            else:
                                print("!")
                        elif open_arcane_journal.lower() == "no":
                            print("You decided not to open the journal, I suppose it is good to respect peoples privacy.")
                            work_bench_choice_two = str(input("""Would you like to:
                                                                 A: Examine the map
                                                                 B: Examine the bell
                                                                 C: Examine the rotting piece of wood
                                                             """))
                            if work_bench_choice_two.lower() == "a":
                                print("You decided to inspect the map, it is too faded to dechiper. If only you had the right tools...")
                                take_faded_map = str(input("Would you like to take the map? "))
                            elif work_bench_choice_two.lower() == "b":
                                print("You decided to inspect the bell, there appears to be a hole rusted through the side so it probably will not work.")
                                take_rusted_bell = str(input("Would you like to take the bell? "))
                            elif work_bench_choice_two.lower() == "c":
                                print("It appears that there is a rotting piece of wood on the table")
                                take_rotting_wood = str(input("Would you like to take the rotting wood? "))
                            else:
                                print("!")
                        else:
                            print("!")
                    else:
                        print("I am really getting tired of writing these error statements")
                elif inspect_workbench.lower() == "no":
                    print("You decided that you didn't want to inspect the workbench, I'm sure there is nothing crucial on the table.")
                    print("As you continue to look around the room you come to the conclusion that there is only two options:")
                    go_downstairs = str(input("""Would you like to:
                                                A: Go Downstairs
                                                B: Try to wake the boy up
                                             """))
                else:
                    print("Either I am not very good a programming, or you are terrible at following basic instructions.")
            elif take_bag.lower() == "no":
                print("You decided to not take the bag, fair enough")
                inspect_workbench = input("As you look around you, you see an assortment of items on a workbench next to the boys bed. Would you like to inspect the workbench?")
            else:
                print("Either I am not very good at programing, or you are not very good at following basic instructions.")
        elif wake_up.lower() == "b":
            print("""Unable to overcome the exhaustion you fall back into slumber. You stray out of thought, and mind where each day is a life age of the earth.
                 Suddenly you are awoken by the small child. 'Wake up, wake up!', he cried. 'You must hurry, the master of the tavern requests to speak with you, although
                 if I were you I might want to bring you bag, things might get ugly.
            """)
            take_bag = str(input("Would you like to take the bag on your bedside table, as the boy suggests?"))
        else:
            print("It appears something has gone wrong, also while I have you here can I talk to you about your cars extended warrenty.")
