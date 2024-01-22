import os

def get_directory_names(directory_path):
    if not os.path.isdir(directory_path):
        print(f"{directory_path} is not a valid directory path.")
        return
    
    names = os.listdir(directory_path)
    sorted_names = sorted(names, key=lambda x: x.lower())
    
    return sorted_names

directory_path = 'D:\\Valerian\\Coding\\Python\\Personal Projects\\Index Shifter\\SongTest'
names_list = get_directory_names(directory_path)
for name in names_list:
    print(name)