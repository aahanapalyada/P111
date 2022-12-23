import os
import shutil

from_dir = "/Users/kiranpalyada/Downloads"
to_dir = "/Users/kiranpalyada/Desktop/Document_Files"

list_of_files = os.listdir(from_dir)

for files in list_of_files:
    root, ext = os.path.splitext(files)
    print(root,ext)

