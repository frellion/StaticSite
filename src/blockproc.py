from enum import Enum

BlockType = Enum('BlockType', ['paragraph', 'heading', 'code', 'quote', 'unordered_list', 'ordered_list'])


def block_to_block_type(md):
	md_array = md.split("\n")
	if md[0:2]=="# " or md[0:3]=="## " or md[0:4]=="### " or md[0:5]=="#### " or md[0:6]=="##### "or md[0:7]=="###### ":
		return BlockType.heading
	elif md[0:3] == "```" and md[-3:] == "```":
		return BlockType.code
	elif md[0] == ">":
		is_quote = True
		for string in md_array:
			if string[0]!=">":
				is_quote = False
		if is_quote:
			return BlockType.quote
	elif md[0:2] == "- ":
		is_ul = True
		for string in md_array:
			if string[0:2]!="- ":
				is_ul = False
		if is_ul:
			return BlockType.unordered_list
	elif md[0:3] == "1. ":
		is_ol = True
		for string in range(0,len(md_array)-1):
			if md_array[string].split(". ",1)[0]!=f"{string+1}":
				is_ol = False
		if is_ol:
			return BlockType.ordered_list
	else:
		return BlockType.paragraph
