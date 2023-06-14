import math

class InputUtility:

    def __init__(self):
        # Smoke wit me, drink wit me
        pass

    def string(self, user_input: str) -> str:

        user_input = str(user_input).capitalize().strip()

        return user_input

    def integer(self, user_input: int | float, data_type: float, round_precision: str | None = None) -> int | float:

        if round_precision == None:
            pass
        elif round_precision == 'Tenth':
            return math.ceil(user_input / 10) * 10
        elif round_precision == 'Hundreth':
            return math.ceil(user_input / 100) * 100
        elif round_precision == 'Thousenth':
            return math.ceil(user_input / 1000) * 1000
        else:
            pass

        if data_type == 'int':
            user_input = int(user_input)
        elif data_type == 'float':
            user_input = float(user_input)
        else:
            pass

        return user_input