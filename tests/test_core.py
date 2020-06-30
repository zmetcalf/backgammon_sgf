import os

from pytest import raises

from backgammon_sgf.core import parse_file
from backgammon_sgf.sgf_tree import SgfTree

def test_open():
    assert isinstance(parse_file(
        os.path.join(
            os.path.dirname(__file__),
            'gnubg_file.sgf'
        )
    ), SgfTree)

def test_open_not_found():
    with raises(FileNotFoundError):
        parse_file('yo, not here brah')
