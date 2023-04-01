import os, shutil

from_dir = "C:/Users/azanz/Downloads"
to_dir = "C:/Users/azanz/OneDrive/Desktop/byjus/project-102/Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)
types_of_files = []

for file in list_of_files:
    root, ext = os.path.splitext(file)
    if ext == "":
        continue
    if ext not in types_of_files:
        types_of_files.append(ext)
        os.mkdir("C:/Users/azanz/OneDrive/Desktop/byjus/project-102/Document_Files/" + ext)
    shutil.move(from_dir + "/" + file, to_dir + "/" + ext)

