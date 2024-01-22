import os
from natsort import natsorted

def get_file_names(directory_path):
    if not os.path.isdir(directory_path):
        print(f"{directory_path} is not a valid directory path.")
        return
    
    names = os.listdir(directory_path)
    names = natsorted(names)
    return names

directory_path = 'D:\\Valerian\\Coding\\Python\\Personal Projects\\Index Shifter\\SongTest'
file_names = get_file_names(directory_path)
for name in file_names:
    print(name)