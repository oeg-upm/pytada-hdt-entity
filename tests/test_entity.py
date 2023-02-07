import unittest
from tada_hdt_entity.entity import EntityAnn
from tada_hdt_entity.parser import Parser
import os


class TestEntity(unittest.TestCase):
    def test_entity(self):
        ea = EntityAnn()
        self.assertIsNotNone(ea)

if __name__ == '__main__':
    unittest.main()
