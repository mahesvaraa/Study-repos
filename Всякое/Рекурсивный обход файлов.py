import os

path = '/'


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


obhod_file(path)
