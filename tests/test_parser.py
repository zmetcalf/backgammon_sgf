import os

import unittest

from pytest import fixture

from backgammon_sgf.parser import Parser
from backgammon_sgf.sgf_tree import SgfTree

@fixture
def gnubg_file():
    file_path = os.path.join(
        os.path.dirname(__file__),
        'gnubg_file.sgf'
    )

    with open(file_path) as f:
        data = f.read()
    return data

def test_split_matches(gnubg_file):
    assert isinstance(Parser.parse(gnubg_file), SgfTree)


class SgfParsingTest(unittest.TestCase):
    # Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0
    # Test from exercism.io https://exercism.io/my/solutions/ed602516bc184edb99f5a04bc40b57ee
    def test_empty_input(self):
        input_string = ""
        with self.assertRaisesWithMessage(ValueError):
            Parser.parse(input_string)

    def test_tree_with_no_nodes(self):
        input_string = "()"
        with self.assertRaisesWithMessage(ValueError):
            Parser.parse(input_string)

    def test_node_without_tree(self):
        input_string = ";"
        with self.assertRaisesWithMessage(ValueError):
            Parser.parse(input_string)

    def test_node_without_properties(self):
        input_string = "(;)"
        expected = SgfTree()
        self.assertEqual(Parser.parse(input_string), expected)

    def test_single_node_tree(self):
        input_string = "(;A[B])"
        expected = SgfTree(properties={"A": ["B"]})
        self.assertEqual(Parser.parse(input_string), expected)

    def test_multiple_properties(self):
        input_string = "(;A[b]C[d])"
        expected = SgfTree(properties={"A": ["b"], "C": ["d"]})
        self.assertEqual(Parser.parse(input_string), expected)

    def test_properties_without_delimiter(self):
        input_string = "(;A)"
        with self.assertRaisesWithMessage(ValueError):
            Parser.parse(input_string)

    def test_all_lowercase_property(self):
        input_string = "(;a[b])"
        with self.assertRaisesWithMessage(ValueError):
            Parser.parse(input_string)

    def test_upper_and_lowercase_property(self):
        input_string = "(;Aa[b])"
        with self.assertRaisesWithMessage(ValueError):
            Parser.parse(input_string)

    def test_two_nodes(self):
        input_string = "(;A[B];B[C])"
        expected = SgfTree(properties={"A": ["B"]}, children=[SgfTree({"B": ["C"]})])
        self.assertEqual(Parser.parse(input_string), expected)

    def test_two_child_trees(self):
        input_string = "(;A[B](;B[C])(;C[D]))"
        expected = SgfTree(
            properties={"A": ["B"]},
            children=[SgfTree({"B": ["C"]}), SgfTree({"C": ["D"]})],
        )
        self.assertEqual(Parser.parse(input_string), expected)

    def test_two_trees(self):
        input_string = "(;B[C](;E[F])(;G[H]))(;C[D])"
        expected = [
            SgfTree(
                properties={"B": ["C"]},
                children=[],
            ),
            SgfTree(
                properties={"C": ["D"]},
                children=[],
            ),
        ]
        # expected = SgfTree(
        #     properties={},
        #     children=[SgfTree({"B": ["C"]}), SgfTree({"C": ["D"]})],
        # )
        # self.assertEqual(Parser.parse(input_string).children[0].properties, {})
        self.assertEqual(Parser.parse(input_string), expected)

    def test_multiple_property_values(self):
        input_string = "(;A[b][c][d])"
        expected = SgfTree(properties={"A": ["b", "c", "d"]})
        self.assertEqual(Parser.parse(input_string), expected)

    def test_escaped_property(self):
        input_string = "(;A[\\]b\nc\nd\t\te \n\\]])"
        expected = SgfTree(properties={"A": ["]b\nc\nd  e \n]"]})
        self.assertEqual(Parser.parse(input_string), expected)

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == "__main__":
    unittest.main()
