import unittest
from tada_hdt_entity import graph


class TestGraph(unittest.TestCase):
    def test_graph(self):
        g = graph.Graph("logger_test.log")
        g.add_node("test_node")
        g.print_nodes()
        self.assertIsNotNone(g)

if __name__ == '__main__':
    unittest.main()