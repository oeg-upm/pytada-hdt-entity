import unittest
from tada_hdt_entity.parser import Parser


class TestParser(unittest.TestCase):
    def test_parser(self):
        p = Parser("test.csv")
        data = p.parse_vertical()
        self.assertIsNotNone(p)


if __name__ == '__main__':
    unittest.main()