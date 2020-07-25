import re

class Parser:
    def __init__(self, data):
        self.data = data
        self.matches = []

        # Iterator Items
        self.current_string = ''
        self.parent = None
        self.key = None
        self.in_list = False


    @classmethod
    def parse(cls, data):
        return Parser(data).build_model()

    def build_model(self):
        self.clean_data()

        for index, char in enumerate(self.data):
            # TODO Handle escapes
            # TODO Validate that starts with (
            # TODO Refactor into method list that has methods that return
            #       true to continue and false to fall through.
            #       Be careful to continue Parent loop

            # Match Start
            if not self.parent and char == '(' and self.data[index + 1] == ';':
                self.parent = {}
                self.matches.append(self.parent)
                continue

            # Match already started
            if char == ';' and index > 0 and self.data[index - 1] == '(':
                continue

            # Building current string
            if char != ';' or (char != '[' and self.data[index - 1] != '\\'):
                self.current_string += char
                continue

            # Set property key
            if char == '[' and self.data[index - 1] != '\\':
                self.key = self.current_string
                self.parent['properties'][self.key] = ''
                self.current_string = ''
                continue

            # Set Non-List Value
            if char == ']' and not self.in_list and self.data[index - 1] != '\\' and self.data[index + 1] != '[':
                self.parent['properties'][self.key] = self.current_string
                self.current_string = ''
                self.key = None
                continue

            # Set List Value
            if char == ']' and (self.in_list or self.data[index + 1] == '['):
                if self.parent['properties'][self.key] == '':
                    self.parent['properties'][self.key] = [self.current_string]
                    self.current_string = ''
                    continue

                self.parent['properties'][self.key].append(self.current_string)
                self.current_string = ''
                continue

            # Set Nodes
            if char == ';' and not self.data[index - 1] == ';':
                nodes = self.parent.get('nodes', [])
                ## How do we start getting

            # Set children
            if char == '(' and self.data[index + 1] == ';' and self.parent is not None:
                pass


    def clean_data(self):
        self.data = self.data.replace('\n', '').replace('\r', '').replace('\t', ' ').strip()
