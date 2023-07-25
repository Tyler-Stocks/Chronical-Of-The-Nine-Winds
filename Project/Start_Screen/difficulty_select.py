from json import dumps
from Project.IO.choice_Input import get_str_choice

def get_difficulty():
    with open('data/difficulty.json') as f:
        f.write(dumps({'Difficulty': get_str_choice('Select Difficulty:\na.) Easy\nb.) Normal\nc.) Hard\nd.) Nightmare\n', ['a', 'b', 'c', 'd'])}))
