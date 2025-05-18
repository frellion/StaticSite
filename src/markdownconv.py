import re
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
#		print(f"node is {node}")
#		old_node_type = node.text_type
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
		else:
			split_node = node.text.split(delimiter)
			#see big block o' logic below
			fragment_count = len(split_node)
			if split_node[0]=="" and split_node[-1]=="":
				#there are 2 extra empty strings to ignore. There should be odd fragments
				fragment_count -= 2
				if fragment_count % 2 == 0:
					raise Exception(f"invalid markdown in {node}")
			elif split_node[0]=="":
				#there is 1 extra empty string to ignore in both cases. There should be even fragments
				fragment_count -=1
				if fragment_count % 2 == 1:
					raise Exception(f"invalid markdown in {node}")
			elif split_node[-1]=="":
				fragment_count -=1
				if fragment_count % 2 == 1:
					raise Exception(f"invalid markdown in {node}")


			for frag_num in range(0, len(split_node)):
				"""
				Because of the delimiter, the odd fragments will be the node's original type.
				If the text starts with the delimiter, the first fragment will be an empty string.
				
				However, this makes it harder to tell if the the delimiters are paired (this is a later
				requirement given, hidden in the exercise tips, since valid markdown syntax requires a 
				closing delimiter.)

				If paired delimiters are all internal, there is an odd number of fragments.
				
				Starting with a delimiter adds an empty string to the beginning of the list. Ending 
				with one adds one to the end. These additional empty strings need to be considered 
				(discarded will be better.)
				"""
				if frag_num % 2 == 0:
					if split_node[frag_num] != "":
						new_nodes.append(TextNode(f"{split_node[frag_num]}", node.text_type))
				else:
					if split_node[frag_num] != "":
						new_nodes.append(TextNode(f"{split_node[frag_num]}", text_type))

	return new_nodes


def extract_markdown_images(text):
	image_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)" , text)
	return image_matches

def extract_markdown_links(text):
	link_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
	return link_matches


def split_nodes_image(old_nodes):
	new_nodes = []
	for old_node in old_nodes:
		images = extract_markdown_images(old_node.text)
		if images ==[]:
			new_nodes.append(old_node)
		else:
			text_to_split = old_node.text
			for image in images:
#				print(f"image is {image}")
#				print(f"text_to_split is {text_to_split}")
				text_pieces = text_to_split.split(f"![{image[0]}]({image[1]})", 1)
				if text_pieces[0]!="":
					new_nodes.append(TextNode(text_pieces[0], TextType.TEXT))
				new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
				if len(text_pieces)>1:
					text_to_split = text_pieces[1]
				if image==images[-1]:
					new_nodes.append(TextNode(text_pieces[1], TextType.TEXT))
#				if len(text_pieces)>1:
#					split_nodes_image([TextNode(text_pieces[1], TextType.TEXT)])
				
					

	return new_nodes


def split_nodes_link(old_nodes):
	new_nodes = []
	for old_node in old_nodes:
		links = extract_markdown_links(old_node.text)
		if links ==[]:
			new_nodes.append(old_node)
		else:
			text_to_split = old_node.text
			for link in links:
				text_pieces = text_to_split.split(f"[{link[0]}]({link[1]})", 1)
				if text_pieces[0]!="":
					new_nodes.append(TextNode(text_pieces[0], TextType.TEXT))
				new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
				if len(text_pieces)>1:
					text_to_split = text_pieces[1]
				if link==link[-1]:
					new_nodes.append(TextNode(text_pieces[1], TextType.TEXT))
#
#				if len(text_pieces)>1:
#					split_nodes_link([TextNode(text_pieces[1], TextType.TEXT)])

	return new_nodes


def text_to_textnodes(text):
	new_nodes = []
	new_nodes.append(TextNode(text, TextType.TEXT, None))
	new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
	new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
	new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
	new_nodes = split_nodes_image(new_nodes)
	new_nodes = split_nodes_link(new_nodes)

	return new_nodes


def markdown_to_blocks(markdown):
	raw_blocks = []
	blocks = []
	raw_blocks = markdown.split("\n\n")
	for raw_block in raw_blocks:
		if raw_block != "":
			blocks.append(raw_block.strip())
	return blocks


"""
def main():
#	text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
	text = "This is _italic_ and **bold** with a [link](https://boot.dev) and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) at the end."
	print(text_to_textnodes(text))
#	text_to_textnodes(text)

main()
"""
