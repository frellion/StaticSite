#from textnode import TextNode
#from textnode import TextType
import sys
from generate import *


def main():
#	test = TextNode("This is a test", TextType.ITALIC, "www.whatever.com")
#	print(test)
#	if sys.argv[1]!="" and sys.argv[1]!= None:
#		basepath = sys.argv[1]
#	else:
#		basepath = "/"
	if len(sys.argv)>1:
		basepath = sys.argv[1]
	else:
		basepath = "/"

	set_up_public()
	dir_path_content = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/content/"
#	dest_dir_path = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/public/"
	dest_dir_path = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/docs/"
	template_path = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/template.html"
#	generate_pages_recursively(dir_path_content, template_path, dest_dir_path)
	generate_pages_recursively(basepath, dir_path_content, template_path, dest_dir_path)


main()
