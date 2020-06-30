import os

from pytest import fixture

from backgammon_sgf.parser import Parser

@fixture
def gnubg_file():
    file_path = os.path.join(
        os.path.dirname(__file__),
        'gnubg_file.sgf'
    )

    with open(file_path) as f:
        data = f.read()
    return data

def test_split_matches(gnubg_file):
    assert len(Parser.parse(gnubg_file)) == 2

def test_game_data_setup(gnubg_file):
    # assert Parser.parse(gnubg_file)
    pass

def test_move_setup(gnubg_file):
    pass
