#Work in progress
#script to find certain file type in folder (and subfolders) and remove
import os

directory = "<path to folder>"
route = os.listdir(directory)

for item in route:
    if item.endswith("<ext name>"):
        os.remove(os.path.join(directory, item))