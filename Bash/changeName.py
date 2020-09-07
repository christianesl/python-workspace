import sys
import subprocess

name_file = sys.argv[1]

with open(name_file) as file:
	for old_doc in file:
		new_doc = old_doc.strip()
		new_doc.replace("jane_", "jdoe_")
		subprocess.run([mv ,old_doc, new_doc])
print("finish")