import os

from backgammon_sgf.parser import Parser

def parse_file(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f'{path} is not found')
    with open(path) as f:
        data = f.read()
    return Parser.parse(data)

def write_file(games):
    pass
