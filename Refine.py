from Windows import get_file_names, rename_file

directory_path = input('Enter the Folder Location : ')
file_names = get_file_names(directory_path)

zFill = int(input('Enter the Number of Digits : '))

for index, file_name in enumerate(file_names):
    old_file_name = directory_path + '\\' + file_name
    new_file_name = directory_path + '\\' + str(index+1).zfill(zFill) + ' ' + file_name.split(maxsplit=1)[1]
    rename_file(old_file_name, new_file_name)