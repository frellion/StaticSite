from enum import Enum
from textnode import *

class HTMLNode:
	def __init__(self, tag = None, value = None, children = None, props = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		html = ""
		for prop in self.props:
			html+=f" {prop}="
			html+=f"\"{self.props[prop]}\""
		return html

	def __repr__(self):
		nl = "\n"
		return f"tag = {self.tag}{nl}value = {self.value}{nl}children = {self.children}{nl}props = {self.props}"


class ParentNode(HTMLNode):
	def __init__(self, tag, children, props = None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		#missing parameter handling
		if self.tag == None or self.tag == "":
			raise ValueError("ParentNode requires a tag")
		if self.children == None or self.children == "":
			raise ValueError("ParentNode requires children")

		for child in self.children:
			if self.props==None or self.props=="":
				open_tag = f"<{self.tag}>"
			else:
				open_tag = f"<{self.tag}{self.props_to_html()}>"

			close_tag = f"</{self.tag}>"
			return open_tag+child.to_html()+close_tag

"""
		for x in range(0, len(self.children)-1):
			#open and close tags
			if self.props==None or self.props=="":
				open_tag = f"<{self.tag}>"
			else:
				open_tag = f"<{self.tag}{self.props_to_html()}>"

			close_tag = f"</{self.tag}>"

			#recursive step <yay -_-*>
			return open_tag+children[x].to_html()+closing_tag
"""


class LeafNode(HTMLNode):
	def __init__(self, value, tag = None, props = None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value==None:
			raise ValueError("LeafNode require a value")
		if self.tag==None:
			return self.value
		else:
			close_tag = f"</{self.tag}>"
			if self.props==None or self.props=="":
				open_tag = f"<{self.tag}>"
			else:
				open_tag = f"<{self.tag}{self.props_to_html()}>"
		return open_tag+self.value+close_tag

def text_node_to_html_node(text_node):
	match text_node.text_type:
		case TextType.TEXT:
			return LeafNode(text_node.text)
		case TextType.BOLD:
			return LeafNode(text_node.text, "b")
		case TextType.ITALIC:
			return LeafNode(text_node.text, "i")
		case TextType.CODE:
			return LeafNode(text_node.text, "code")
		case TextType.LINK:
#			return LeafNode(text_node.text, "a", {"href": f"\"{text_node.url}\""})
			return LeafNode(text_node.text, "a", {"href": f"{text_node.url}"})
		case TextType.IMAGE:
#			return LeafNode("", "img", {"src": f"\"{text_node.url}\"", "alt": f"\"{text_node.text}\""})
			return LeafNode("", "img", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
		case _:
			raise Exception("Not a valid node")
