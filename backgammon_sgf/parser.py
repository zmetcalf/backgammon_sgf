import re

class Parser:
    def __init__(self, data):
        self.data = data
        self.matches = []

    @classmethod
    def parse(cls, data):
        return Parser(data).build_model()

    def build_model(self):
        self.clean_data()

        current_string = ''
        for index, char in enumerate(self.data):
            # TODO Handle escapes
            pass


    def clean_data(self):
        self.data = self.data.replace('\n', '').replace('\r', '').replace('\t', ' ')