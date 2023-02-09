import unittest
from tada_hdt_entity import tnode


class TestParser(unittest.TestCase):
    def test_parser(self):
        tn2 = tnode.TNode("as")
        self.assertIsNotNone(tn2)


if __name__ == '__main__':
    unittest.main()