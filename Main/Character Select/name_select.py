class MainNameSelect():

    class Name_Select():

        def __init__(self):

            self.name = ''

        def ask_user_name(self):

            while True:

                    self.name = input(f'Hello my friend, what might your name be?\n')

                    try:

                        if self.name.isspace():
                            print(f'Please enter a game.\n')


                        elif self.name.isnumeric():
                            print(f'You cannot enter a number as your name.\n')

                        else:
                            name_confirmation = input(f'So your name is {self.name}?\n')

                            try:

                                if name_confirmation.lower() != 'no':
                                    print(f'Interesting, very interesting.\n')
                                    break

                                else:
                                    continue

                            except ValueError:
                                raise ValueError

                    except ValueError:
                        raise ValueError

            return self.name

    Name_Select_Obj = Name_Select()

    Name = Name_Select_Obj.ask_user_name()