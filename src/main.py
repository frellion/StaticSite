#from textnode import TextNode
#from textnode import TextType
from generate import *

def main():
#	test = TextNode("This is a test", TextType.ITALIC, "www.whatever.com")
#	print(test)
	set_up_public()
	from_path = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/content/index.md"
	dest_path = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/public/index.html"
	template_path = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/template.html"
	generate_page(from_path, template_path, dest_path)
main()
