from sgfmill.sgf import Sgf_game

class Parser:
    def __init__(self, data):
        self.data = data
        self.matches = []

    @classmethod
    def parse(cls, data):
        return Parser(data).build_model()

    def build_model(self):
        self.matches = Sgf_game.from_string(self.data).serialise()
        return self.matches
