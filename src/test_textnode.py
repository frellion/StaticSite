import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node = TextNode("This is a text node", TextType.BOLD)
		node2 = TextNode("This is a text node", TextType.BOLD)
		self.assertEqual(node, node2)
	
	def test_notEq(self):
		node2 = TextNode("This is a text node", TextType.BOLD)
		node3 = TextNode("This is'nt a text node", TextType.BOLD)
		self.assertNotEqual(node2, node3)

	def test_default(self):
		node2 = TextNode("This is a text node", TextType.BOLD)
		node4 = TextNode("This is a text Node", TextType.BOLD, None)
		self.assertEqual(node2, node4)

	def assertEqual(self, node1, node2):
		if node1==node2:
			return True
		return False

	def assertNotEqual(self, node1, node2):
		if node1==node2:
			return False
		return True

if __name__ == "__main__":
	unittest.main()
