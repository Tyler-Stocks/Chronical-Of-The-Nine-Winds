class MainNameSelect():

    class NameSelect():

        def __init__(self):

            self.name = ''

        def ask_user_name(self):

            while True:

                self.name = input('Hello my friend, what might your name be?\n')

                try:

                    if self.name.isspace():
                        print('Please enter a game.\n')


                    elif self.name.isnumeric():
                        print('You cannot enter a number as your name.\n')

                    else:
                        name_confirmation = input(f'So your name is {self.name}?\n')

                        try:

                            if name_confirmation.lower() != 'no':
                                print('Interesting, very interesting.\n')
                                break

                            else:
                                continue

                        except ValueError as exc:
                            raise ValueError from exc

                except ValueError as exc:
                    raise ValueError from exc

            return self.name

    Name_Select_Obj = NameSelect()

    Name = Name_Select_Obj.ask_user_name()
