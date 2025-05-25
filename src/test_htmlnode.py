import unittest

#from htmlnode import HTMLNode
#from htmlnode import LeafNode
#from htmlnode import ParentNode
from htmlnode import *
from textnode import *



def assertEqual(string1, string2):
	if string1==string2:
		return True
	return False


class TestHTMLNode(unittest.TestCase):
	def test_props_to_html(self):
		node = HTMLNode("a", "This is a test HTML Node", None, {"href":"https://www.google.com", "target":"_blank"})
#		print(node)
#		self.assertEqual(node.props_to_html()," href=\"https://www.google.com\" target=\"_blank\"")
		assertEqual(node.props_to_html()," href=\"https://www.google.com\" target=\"_blank\"")
"""
	def assertEqual(self, string1, string2):
		if string1==string2:
			return True
		return False
"""

class TestLeafNode(unittest.TestCase):

	def test_leaf_to_html_p(self):
#		node = LeafNode("p", "Hello, world!")
		node = LeafNode("Hello, world!", "p")
#		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
		assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_leaf_to_html_a(self):
#		node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})
		node = LeafNode("Click me!", "a", {"href": "https://www.google.com", "target": "_blank"})
#		self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Click me!</a>")
		assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Click me!</a>")

	def test_text(self):
		node = TextNode("This is a text node", TextType.TEXT)
#		print(f"troublesome node: {node}")
		html_node = text_node_to_html_node(node)
#		self.assertEqual(html_node.tag, None)
#		self.assertEqual(html_node.value, "This is a text node")
		assertEqual(html_node.tag, None)
		assertEqual(html_node.value, "This is a text node")


"""
	def assertEqual(self, string1, string2):
		if string1==string2:
			return True
		return False
"""


class TestParentNode(unittest.TestCase):
	def test_to_html_with_children(self):
#		child_node = LeafNode("span", "child")
		child_node = LeafNode("child", "span")
		parent_node = ParentNode("div", [child_node])
#		print(f"html with children: {parent_node}")
#		print(f"parent_node is {parent_node}")
#		print(f"leaf is {child_node}")
#		print(f"leaf html is {child_node.to_html()}")
#		print(f"parent html is {parent_node.to_html()}")
#		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
		assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
#		grandchild_node = LeafNode("b", "grandchild")
		grandchild_node = LeafNode("grandchild", "b")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
#		print(f"html with grandchildren: {parent_node}")
#		self.assertEqual(
#			parent_node.to_html(),
 #			"<div><span><b>grandchild</b></span></div>",
#		)
		assertEqual(
			parent_node.to_html(),
 			"<div><span><b>grandchild</b></span></div>",
		)


"""
	def assertEqual(self, string1, string2):
		if string1==string2:
			return True
		return False
"""
