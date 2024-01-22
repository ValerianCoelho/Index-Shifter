from Windows import get_file_names

directory_path = 'D:\\Valerian\\Coding\\Python\\Personal Projects\\Index Shifter\\SongTest'
file_names = get_file_names(directory_path)
for name in file_names:
    print(name)