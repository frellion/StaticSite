#CH5 L1
import os
import shutil

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
				#print(f"deleting {item_path}")
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
				#print(f"from {item_source_path}")
				#print(f"to {item_dest_path}")
				shutil.copy(item_source_path, item_dest_path)
			else:
				#print(f"from folder {item_source_path}")
				#print(f"to folder {item_dest_path}")
				os.mkdir(item_dest_path)
				copy_files(item_source_path, item_dest_path)

