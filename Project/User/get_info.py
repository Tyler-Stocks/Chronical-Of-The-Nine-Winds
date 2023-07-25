from json import dumps
from Project.IO.raw_input import get_str, get_int

def get_age() -> str:
    return dumps({
        'Age': get_int('How old are you?', 1, 100)
    })

def get_gender() -> str:
    return dumps({
        'Gender': get_str('What is your gender?', 1, 20),
        'First Pronoun': get_str('What is your first pronoun?', 1, 10),
        'Second Pronoun': get_str('What is your second pronoun?', 1, 10),
    })

def get_name() -> str:
    return dumps({
        'First Name': get_str('What is your first name?', 1, 50),
        'Middle Name': get_str('What is your middle name?', 1, 50),
        'Last Name': get_str('What is your last name?', 1, 50),
    })

def format_user_info() -> str:
    return dumps({
        'Age Information': get_age(),
        'Name Information': get_name(),
        'Gender Information': get_gender(),
    })

def get_user_info() -> None:
    with open('data/user_info.json', 'w') as f:
        f.write(format_user_info())
