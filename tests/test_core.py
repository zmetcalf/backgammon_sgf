import os

from pytest import raises

from backgammon_sgf.core import parse_file

def test_open():
    assert len(parse_file(
        os.path.join(
            os.path.dirname(__file__),
            'gnubg_file.sgf'
        )
    )) == 2

def test_open_not_found():
    with raises(FileNotFoundError):
        parse_file('yo, not here brah')
