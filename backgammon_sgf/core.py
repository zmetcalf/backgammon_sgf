import os

from backgammon_sgf.parser import Parser

def parse_file(path, replace_keys=False):
    if not os.path.isfile(path):
        raise FileNotFoundError(f'{path} is not found')
    with open(path) as f:
        data = f.read()
    return Parser.parse(data, replace_keys)

def write_file(games):
    pass
