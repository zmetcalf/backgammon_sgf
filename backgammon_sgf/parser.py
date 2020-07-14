import re

from backgammon_sgf.sgf_tree import SgfTree

class Parser:
    def __init__(self, data):
        self.data = data

    @classmethod
    def parse(cls, data):
        return Parser(data).build_model()

    def build_model(self):
        return self.get_tree()

    def get_tree(self):
        # https://exercism.io/tracks/python/exercises/sgf-parsing/solutions/054af0b8cf794cc78047fbea5cd55d00
        input_string = self.data.replace("\\", "").replace("\t", " ")    # To remove escape sequence
        _trees = self.find_trees(input_string)                           # Find trees > remove ()
        _nodes = self.find_node(_trees)                                  # Find nodes and put through parser

        return list(map(lambda node: self.build_node_tree(node), _nodes))

    def build_node_tree(self, node):
        _nodes = self.find_node(node)                                    # Find nodes and put through parser
        _properties = _nodes[0]
        if len(_nodes) > 1:                                              # Including children
            _children = [SgfTree(_nodes[i + 1]) for i in range(len(_nodes) - 1)]
            return SgfTree(properties = _properties, children = _children)
        return SgfTree(properties = _properties)                         # Only properties


    def find_trees(self, input):                                         # Check syntax and make into tree
        pat_correct = re.compile(r'''\(;                                 # Added ; so it can be empty
        ([A-Z]*(\[[\W\w]+\])+)*                                          # Possible first node
        (;([A-Z]*(\[[\W\w]+\])+)*)*                                      # Possible children
        (\((;([A-Z]*(\[[\W\w]+\])+)*)*\))*                               # Possible children trees
        \)''', re.VERBOSE)
        if pat_correct.search(input) == None:
            raise ValueError('Pattern incorrect!')
        pat_tree = re.compile(r'(?<=\()[\W\w]*(?=\))')
        trees = pat_tree.search(input).group()
        return trees

    def find_node(self, tree):                                           # Finds notes and gets their properties
        pat_node = re.compile(r'(;[\W\w]+?)(?=;|$)')
        nodes = pat_node.findall(tree)
        for i in range(len(nodes)):
            nodes[i] = self.find_properties(nodes[i])
        return nodes

    def find_properties(self, node):                                     # Outputs properties dicts: {"A": ["b", "c"], "D": ["e"]}
        pat_prop = re.compile(r'(\w+)((\[[\W\w]+?\](?!\]))*)')
        props = pat_prop.findall(node)
        props_dict = {}
        for i in range(len(props)):
            props_dict[props[i][0]] = re.findall(r'(?<=\[)[\W\w]+?(?=\]\[|.$)', props[i][1])
        return props_dict

