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
    assert len(Parser.parse(gnubg_file, False)) == 2

def test_deserialize_keys(gnubg_file):
    # assert Parser.parse(gnubg_file, False)
    pass
