#CH5 L1
import os
import shutil
from markdownconv import *

def set_up_public():
	source = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/static"
	dest = "/mnt/c/Users/frellion/Projects/staticsite/StaticSite/public"

	delete_files(dest)
	copy_files(source, dest)


def delete_files(location):
	if os.path.exists(location):
		list = os.listdir(location)
		for item in list:
			item_path = os.path.join(location, item)
			if os.path.isfile(item_path):
#				print(f"deleting {item_path}")
				os.remove(item_path)
			else:
				delete_files(item_path)
				os.rmdir(item_path)


def copy_files(source, destination):
	if os.path.exists(source):
		list = os.listdir(source)
		for item in list:
			item_source_path = os.path.join(source, item)
			item_dest_path = os.path.join(destination, item)
			if os.path.isfile(item_source_path):
#				print(f"from {item_source_path}")
#				print(f"to {item_dest_path}")
				shutil.copy(item_source_path, item_dest_path)
			else:
				print(f"from folder {item_source_path}")
				print(f"to folder {item_dest_path}")
				os.mkdir(item_dest_path)
				copy_files(item_source_path, item_dest_path)



def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")
	if os.path.exists(from_path) and os.path.isfile(from_path):
		source = open(from_path)
		markdown = source.read()
		source.close()
	if os.path.exists(template_path) and os.path.isfile(template_path):
		source = open(template_path)
		template = source.read()
		source.close()

	title = extract_title(markdown)
	html_nodes = markdown_to_html_node(markdown)
	html = ""
#	for html_node in html_nodes:
#		html += html_node.to_html()
	html = html_nodes.to_html()

#	print(f"title is {title}")
#	print(f"html is {html}")

	template = template.replace("{{ Title }}", title)
	template = template.replace("{{ Content }}", html)

	if os.path.exists(os.path.dirname(dest_path)):
		print(f"dest_path: {dest_path}")
#		file_name = dest_path+".html"
		with open(dest_path, "w") as output:
			output.write(template)
	else:
		os.makedirs(os.path.dirname(dest_path))
#		file_name = dest_path+".html"
		with open(dest_path, "w") as output:
			output.write(template)



def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
#	#template file
#	if os.path.exists(template_path) and os.path.isfile(template_path):
#		source = open(template_path)
#		template = source.read()
#		source.close()

	#source list
	if os.path.exists(dir_path_content) and os.path.isdir(dir_path_content):
		source_list = os.listdir(dir_path_content)


		for source in source_list:
			item_source_path = os.path.join(dir_path_content, source)
			item_dest_path = os.path.join(dest_dir_path, source)
			if os.path.isfile(item_source_path):
				if os.path.isdir(item_dest_path):
					dest_file_name = dest_dir_path+"index.html"
				else:
					#dest_file_name = dest_dir_path+".html"
					dest_file_name = dest_dir_path+"/index.html"
#				generate_page(item_source_path, template_path, dest_dir_path)
#				generate_page(item_source_path, template_path, item_dest_path)
				generate_page(item_source_path, template_path, dest_file_name)

#				#load in and process each; copy into destination folder
#
#				#read markdown
#				source_file = open(item_source_path)
#				markdown = source_file.read()
#				source_file.close()

			else:
				#item_source_path is a directory. Create destination directory and
				#call this whole thing recursively
				print(f"from folder {item_source_path}")
				print(f"to folder {item_dest_path}")
				os.mkdir(item_dest_path)
				generate_pages_recursively(item_source_path, template_path, item_dest_path)

