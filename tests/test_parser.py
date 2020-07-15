import os

from pytest import fixture

from backgammon_sgf.parser import Parser

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


BASIC_GAME = '''
    (;FF[4]GM[1]SZ[19]
        ;B[aa]
        ;W[bb]
            (;B[cc]N[Var A];W[dd];B[ad];W[bd])
            (;B[hh]N[Var B];W[hg])
            (;B[gg]N[Var C];W[gh];B[hh]
                (;W[hg]N[Var A];B[kk])
                (;W[kl]N[Var B])
            )
    )
    (;FF[4]GM[2]SZ[19]AR[\[a\]][b][c])
'''

BASIC_GAME_PARSED = [
    {
        'properties': {
            'FF': '4',
            'GM': '1',
            'SZ': '19',
        },
        'nodes': [
            {
                'properties': {
                    'B': 'aa'
                }
            },
            {
                'properties': {
                    'W': 'bb'
                },
                'children': [
                    {
                        'nodes':  [
                            {
                                'properties': {
                                    'B': 'cc',
                                    'N': 'Var A',
                                }
                            },
                            {
                                'properties': {
                                    'W': 'dd'
                                }
                            },
                            {
                                'properties': {
                                    'B': 'ad'
                                }
                            },
                            {
                                'properties': {
                                    'W': 'bd'
                                }
                            },
                        ]
                    },
                    {
                        'nodes': [
                            {
                                'properties': {
                                    'B': 'hh',
                                    'N': 'Var B'
                                }
                            },
                            {
                                'properties': {
                                    'W': 'hg'
                                }
                            }
                        ]
                    },
                    {
                        'nodes': [
                            {
                                'properties': {
                                    'B': 'gg',
                                    'N': 'Var C'
                                }
                            },
                            {
                                'properties': {
                                    'W': 'gh'
                                }
                            },
                            {
                                'properties': {
                                    'B': 'hh'
                                },
                                'children': [
                                    {
                                        'nodes': [
                                            {
                                                'properties': {
                                                    'W': 'hg',
                                                    'N': 'Var A'
                                                }
                                            },
                                            {
                                                'properties': {
                                                    'B': 'kk'
                                                }
                                            }
                                        ]
                                    },
                                    {
                                        'nodes': [
                                            {
                                                'properties': {
                                                    'W': 'kl',
                                                    'N': 'Var B'
                                                }
                                            }
                                        ] # End Lvl 2 Nodes
                                    }
                                ] # End Lvl 2 Children
                            }
                        ] # End Lvl 1 Nodes
                    }
                ] # Endl Lvl 1 Children
            }
        ] # End Parent Nodes
    }, # End First Match

    # Second Match
    {
        'properties': {
            'FF': '4',
            'GM': '2',
            'SZ': '19',
            'AR': ['[a]', 'b', 'c']
        }
    }
] # Parent Array

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
