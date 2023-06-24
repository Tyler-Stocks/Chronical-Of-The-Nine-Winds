import json
from Project.Utility import integer_input_handling

inputs = integer_input_handling.HandleIntegerInput()

class Age:

    def __init__(self):
        self.age: int = 0

    def query_age(self) -> int:
        self.age: int = inputs.get_int_input('age', 0, 110)
        return self.age

    def format_age(self) -> str:
        age_information: dict[str, int] = {
            'Age': self.age
        }
        age_data: str = json.dumps(age_information, indent = 4)
        return age_data

    def store_age(self) -> None:
        with open('data/age_data.json', 'w') as f:
            f.write(self.format_age())

    def get_age(self) -> None:
        self.query_age()
        self.store_age()

Age().get_age()
