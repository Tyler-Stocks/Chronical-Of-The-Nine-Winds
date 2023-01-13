class Character():
    def __init__(self, name, is_class=False):
        self.name = name
        self.is_class = is_class

class_list = [
    Character('Freelancer', False),
    Character('Explorer', False),
    Character('Knight', False),
    Character('Sage', False),
    Character('Blind Prophet', False)
]

def is_class(character_name):
    for character in class_list:
        if character.name == character_name:
            return character.is_class