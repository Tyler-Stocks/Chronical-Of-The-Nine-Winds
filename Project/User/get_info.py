from json import dumps
from Project.Utility.input import getStr, getInt

def age() -> str:
    return dumps({'Age': getInt('How old are you?', 1, 100)})

def gender() -> str:
    return dumps({
        'Gender': getStr('What is your gender?', 1, 20),
        'First Pronoun': getStr('What is your first pronoun?', 1, 10),
        'Second Pronoun': getStr('What is your second pronoun?', 1, 10),
    })

def name() -> str:
    return dumps({
        'First Name': getStr('What is your first name?', 1, 50),
        'Middle Name': getStr('What is your middle name?', 1, 50),
        'Last Name': getStr('What is your last name?', 1, 50),
    })

def format() -> str:
    return dumps({
        'Age Information': age(),
        'Name Information': name(),
        'Gender Information': gender(),
    })

def get_user_info() -> None:
    with open('data/user_info.json', 'w') as f:
        f.write(format())
