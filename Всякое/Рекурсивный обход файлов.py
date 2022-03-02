import os

pathh = r'C:\Users\danila.shkirdov\Downloads'


def obhod_file(path, level=1):
    print('========================')
    print('Level=', level)
    print('Content:')
    print(*os.listdir(path), sep='\n')

    for i in os.listdir(path):
        if os.path.isdir(path + '\\' + i):
            print('Спускаемся', path + '\\' + i)
            obhod_file(path + '\\' + i, level + 1)
            print('Возвращаемся в', path)
            print('========================')


# obhod_file(path)

def get_file_names(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    file_names = [f.split('\\')[-1] for f in file_paths]

    return file_names


print(get_file_names(pathh))
