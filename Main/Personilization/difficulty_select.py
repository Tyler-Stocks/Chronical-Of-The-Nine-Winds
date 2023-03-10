class DifficultySelector():

    def __init__(self) -> None:

        self.difficulty = ''

    def ask_user_difficulty(self) -> str:

        while True:

            difficultyChoice = input('''Hello there, please select your difficulty:
                                  1. Story
                                  2. Easy
                                  3. Medium
                                  4. Hard
                                  5. NightMare
                              ''')

            try:
                if difficultyChoice.lower() in ('1', 'story'):
                    difficultyConfirmation = input(
                        'Are you sure you would like to choose Story as your difficulty?'
                    )

                    try:
                        if difficultyConfirmation.lower() not in ('n', 'no'):
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif difficultyChoice.lower() in ('2', 'easy'):
                    difficultyConfirmation = input(
                        'Are you sure you would like to choose Easy as your difficulty?'
                    )
                    try:
                        if difficultyConfirmation.lower() not in ('n', 'no'):
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif difficultyChoice.lower() in ('3', 'medium'):
                    difficultyConfirmation = input(
                        'Are you sure you would like to choose Medium as your difficulty?'
                    )

                    try:
                        if difficultyConfirmation.lower() not in ('n', 'no'):
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif difficultyChoice.lower() in ('4', 'hard'):
                    difficultyConfirmation = input(
                        'Are you sure you would like to choose Hard as your difficuly?'
                    )

                    try:

                        if difficultyConfirmation.lower() not in ('n', 'no'):
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif difficultyChoice.lower() in ('5', 'nightmare'):
                    difficultyConfirmation = input(
                        'Are you sure you would like to choose Nightmare as your difficulty?'
                    )

                    try:

                        if difficultyConfirmation.lower() not in ('n', 'no'):
                            break

                        else:
                            continue

                    except ValueError as exc:
                        raise ValueError from exc

                elif difficultyChoice.isspace():
                    print('Please enter a difficulty value.')
                    continue

                elif 0 > int(difficultyChoice) < 5:
                    print(
                        'Please enter a number between 1 and 5 for the difficulty, or the name of the difficulty. For example 1, or Easy.')
                    continue

                else:
                    print('Please enter a valid value for your difficulty.')
                    continue

            except ValueError as exc:
                raise ValueError from exc

        return self.difficulty

DifficultySelect = DifficultySelector()

Difficulty = DifficultySelect.ask_user_difficulty()
