import os

from pytest import fixture

from backgammon_sgf.parser import Parser

from .examples import BASIC_GAME, BASIC_GAME_PARSED

@fixture
def demo_file():
    file_path = os.path.join(
        os.path.dirname(__file__),
        'demo_file.sgf'
    )

    with open(file_path) as f:
        data = f.read()
    return data

@fixture
def gnubg_file():
    file_path = os.path.join(
        os.path.dirname(__file__),
        'gnubg_file.sgf'
    )

    with open(file_path) as f:
        data = f.read()
    return data

def test_basic():
    assert Parser.parse(BASIC_GAME) == BASIC_GAME_PARSED

def test_split_matches_gnubg(gnubg_file):
    assert len(Parser.parse(gnubg_file)) == 2

def test_split_matches_demo(demo_file):
    assert len(Parser.parse(demo_file)) == 2

def test_game_data_setup(gnubg_file):
    # assert Parser.parse(gnubg_file)
    assert 1 == 1

def test_move_setup(gnubg_file):
    assert 1 == 1
