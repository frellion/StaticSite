from textnode import TextNode
from textnode import TextType

def main():
	test = TextNode("This is a test", TextType.ITALIC, "www.whatever.com")
	print(test)

main()
