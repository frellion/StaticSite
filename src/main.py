#from textnode import TextNode
#from textnode import TextType
from generate import *

def main():
#	test = TextNode("This is a test", TextType.ITALIC, "www.whatever.com")
#	print(test)
	set_up_public()
	dir_path_content = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/content/"
	dest_dir_path = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/public/"
	template_path = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/template.html"
	generate_pages_recursively(dir_path_content, template_path, dest_dir_path)


main()
