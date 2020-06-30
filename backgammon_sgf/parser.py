import re

class Parser:
    def __init__(self, data):
        self.data = data
        self.matches = []

    @classmethod
    def parse(cls, data):
        return Parser(data).build_model()

    def build_model(self):
        self.set_matches()
        return self.matches

    def set_matches(self):
        self.matches = list(
            map(lambda element: self.parse_match(element),
                re.findall(r'\(([^)]+)', self.data)
            )
        )

    def parse_match(self, match_data):
        data_and_moves = match_data.split(';')[1:]
        return {
            'detail': self.get_detail(data_and_moves[0:1]),
            'moves': self.get_moves(data_and_moves[1:])
        }

    def parse_match_line(self, line):
        pass

    def get_detail(self, detail):
        pass

    def get_moves(self, moves):
        pass

