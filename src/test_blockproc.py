import unittest
from blockproc import *

class Test_blockTypes(unittest.TestCase):
	def test_paragraph(self):
		md = "This is a paragraph."
		assertEqual(block_to_block_type(md), BlockType.paragraph)

	def test_heading1(self):
		md = "# This is an H1"
		assertEqual(block_to_block_type(md), BlockType.heading)

	def test_heading2(self):
		md = "## This is an H2"
		assertEqual(block_to_block_type(md), BlockType.heading)

	def test_heading3(self):
		md = "### This is an H3"
		assertEqual(block_to_block_type(md), BlockType.heading)

	def test_heading4(self):
		md = "#### This is an H4"
		assertEqual(block_to_block_type(md), BlockType.heading)

	def test_heading5(self):
		md = "##### This is an H5"
		assertEqual(block_to_block_type(md), BlockType.heading)

	def test_heading6(self):
		md = "###### This is an H6"
		assertEqual(block_to_block_type(md), BlockType.heading)

	def test_codeBlock(self):
		md = "```x = 1\nthisThing=\"That thing\"```"
		assertEqual(block_to_block_type(md), BlockType.code)

	def test_unordered_list(self):
		md = "- This is the first item\n- This is the second\n- this is third"
		assertEqual(block_to_block_type(md), BlockType.unordered_list)

	def test_ordered_list(self):
		md = "1. This is the first item\n2. This is the second\n3. this is third"
		assertEqual(block_to_block_type(md), BlockType.ordered_list)

	def test_quote(self):
		md = ">Once upon a midnight dreary\n>While I podered, weak and weary\n>Over many a quaint and curious volume of forgotten lore"
		assertEqual(block_to_block_type(md), BlockType.quote)


def assertEqual(blockType1, blockType2):
	if blockType1==blockType2:
		return True
	return False
