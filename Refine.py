from Windows import get_file_names

directory_path = 'D:\\Valerian\\Coding\\Python\\Personal Projects\\Index Shifter\\SongTest'
file_names = get_file_names(directory_path)
for i in range(len(file_names)):
    new_file_name = str(i+1).zfill(3) + ' ' + file_names[i].split(maxsplit=1)[1]
    print(new_file_name)
    
