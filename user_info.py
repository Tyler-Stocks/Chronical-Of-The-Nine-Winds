class User:
    def __init__(self):
        self.name = ""
        self.age = ""

    def get_info(self):
        while True:
            self.name = input("Hello, what might your name be?\n")
            confirm = input("So your name is " + self.name + "? \n")
            if confirm.lower() == "yes" or confirm.lower() == "y":
                break

        while True:
            self.age = input("How old are you " + self.name + "?\n")
            confirm = input("So you are " + self.age + "?\n")
            if confirm.lower() == "yes" or confirm.lower() == "y":
                break
