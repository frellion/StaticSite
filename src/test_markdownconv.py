import unittest

from markdownconv import *
from textnode import *

class Test_split_nodes_delimiter(unittest.TestCase):
	def test_nodeCreation(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
		self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
		self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))

	def assertEqual(self, textNode1, textNode2):
		if textNode1==textNode2:
			return True
		return False

class Test_extract_markdown(unittest.TestCase):
	def test_extract_markdown_images(self):
		matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

	def test_extract_markdown_links(self):
		matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
		self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")] ,matches)

	def assertListEqual(self, list1, list2):
		if list1==list2:
			return True
		return False


class Test_split_images(unittest.TestCase):
	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
 			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
		[
			TextNode("This is text with an ", TextType.TEXT),
			TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			TextNode(" and another ", TextType.TEXT),
			TextNode(
				"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
			),
		],
		new_nodes,
	)


	def assertListEqual(self, list1, list2):
		if list1==list2:
			return True
		return False


class Test_split_links(unittest.TestCase):
	def test_split_links(self):
		node = TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
 			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
		[
			TextNode("This is text with a link ", TextType.TEXT),
			TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
			TextNode(" and ", TextType.TEXT),
			TextNode(
				"to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
			),
		],
		new_nodes,
	)


	def assertListEqual(self, list1, list2):
		if list1==list2:
			return True
		return False


class Test_text_to_textnodes(unittest.TestCase):
	def test_text_to_textnodes(self):
		text1 = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
		text2 = "This is _italic_ and **bold** with a [link](https://boot.dev) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) at the end."
		new_nodes1 = text_to_textnodes(text1)
		new_nodes2 = text_to_textnodes(text2)
		self.assertListEqual(
		[
			TextNode("This is ", TextType.TEXT),
			TextNode("text", TextType.BOLD),
			TextNode(" with an ", TextType.TEXT),
			TextNode("italic", TextType.ITALIC),
			TextNode(" word and a ", TextType.TEXT),
			TextNode("code block", TextType.CODE),
			TextNode(" and an ", TextType.TEXT),
			TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
			TextNode(" and a ", TextType.TEXT),
			TextNode("link", TextType.LINK, "https://boot.dev"),
		], new_nodes1
		)
		self.assertListEqual(
		[
			TextNode("This is ", TextType.TEXT),
			TextNode("italic", TextType.ITALIC),
			TextNode(" and ", TextType.TEXT),
			TextNode("bold", TextType.BOLD),
			TextNode(" with a ", TextType.TEXT),
			TextNode("link", TextType.LINK, "https://boot.dev"),
			TextNode(" and an ", TextType.TEXT),
			TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
			TextNode(" at the end.", TextType.TEXT)
		], new_nodes2
		)
#		print(new_nodes2)

	def assertListEqual(self, list1, list2):
		if list1==list2:
			return True
		return False

class Test_markdown_to_blocks(unittest.TestCase):
	def test_markdown_to_blocks(self):
		md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

		md_with_spaces = """
  This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line   

- This is a list
- with items
"""

		md_with_empty_blocks = """
This is **bolded** paragraph


This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line




- This is a list
- with items
"""

		blocks = markdown_to_blocks(md)
		blocks_with_spaces = markdown_to_blocks(md_with_spaces)
		blocks_with_empty_blocks = markdown_to_blocks(md_with_empty_blocks)

		assertListEqual(
			blocks,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
				"- This is a list\n- with items",
			],
		)

		assertListEqual(
			blocks_with_spaces,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
				"- This is a list\n- with items",
			],
		)

		assertListEqual(
			blocks_with_empty_blocks,
			[
				"This is **bolded** paragraph",
				"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
				"- This is a list\n- with items",
			],
		)
#		print(blocks)
#		print(blocks_with_spaces)
#		print(blocks_with_empty_blocks)


class Test_block_to_html(unittest.TestCase):
	def test_codeblock(self):
		md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		assertEqual(
			html,
			"<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
		)


	def test_paragraph(self):
		md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		assertEqual(
			html,
			"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
		)


	def test_blockquotes(self):
		md = """
> Let us create a fake quote
> with some fake _emphasis_
> and see what happens.
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		assertEqual(
			html,
			"<div><blockquote>Let us create a fake quote\nwith some fake _emphasis_\nand see what happens.<blockquote></blockquote></div>"
		)


def assertListEqual(list1, list2):
	if list1==list2:
		return True
	return False

def assertEqual(string1, string2):
	if string1==string2:
		return True
	return False
