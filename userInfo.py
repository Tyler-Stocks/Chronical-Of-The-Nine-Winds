def userInfo():
    # Loop ask user for name; Break condition, user inputs yes or y to name confirmation
    while True:
        name = input("Hello, what might your name be?\n")
        confirm = input("So your name is " + name + "? \n")
        if confirm.lower() == "yes" or confirm.lower() == "y":
            break

    # Prints after the user confirms their name
    print("\nInteresting\n")

    # Loop asks user for age; Break condition, user inputs yes or y to age confirmation
    while True:
        age = input("How old are you " + name + "?\n")
        confirm = input("So you are " + age + "?\n")
        if confirm.lower() == "yes" or confirm.lower() == "y":
            break

    # Prints after the user confirms their age
    print("\nI see.\n")
