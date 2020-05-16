import re

class Parser:
    def __init__(self, data, replace_keys):
        self.data = data
        self.matches = []
        self.replace_keys = replace_keys

    @classmethod
    def parse(cls, data, replace_keys):
        return Parser(data, replace_keys).build_model()

    def build_model(self):
        # self.set_matches()
        # self.set_moves()
        for element in re.findall(r'\(([^)]+)', self.data):
            self.matches.append(element)
        return self.matches

    def set_matches(self):
        self.data.replace()
        pass

    def set_moves(self):
        pass
