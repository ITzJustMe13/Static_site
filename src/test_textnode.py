import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node 1", "static")
        node2 = TextNode("This is a text node 2", "bold", "https://google.com")
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()