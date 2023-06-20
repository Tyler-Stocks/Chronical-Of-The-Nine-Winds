import json
import Project.Utility.integer_input_handling

inputs = Project.Utility.integer_input_handling.HandleIntegerInput()

class Age:

    def __init__(self):
        self.age: int = 0

    def get_age(self) -> int:
        self.age: int = inputs.get_int_input('age', 0, 110)
        return self.age

    def format_age(self) -> str:
        age_information: dict[str, int] = {
            'Age': self.age
        }
        age_data: str = json.dumps(age_information, indent = 4)
        return age_data

    def store(self) -> None:
        with open('data/data.json', 'w') as f:
            f.write(self.format_age())

    def main(self) -> None:
        self.get_age()
        self.store()

Age_Obj = Age().main()
