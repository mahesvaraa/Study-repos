import json

dict_one = []
a = input()
data_json = json.dumps(a, indent=4, sort_keys=True)
data_again = eval(json.loads(data_json))
letters = [i['name'] for i in data_again]
for i in data_again:
    arr = f"{i['name']}: {' '.join(i['parents'])}"
    data_json.append(arr)
ddd = {i[0]: i[1:] for i in [j.split(': ') for j in data_json]}
for k, i in ddd.items():
    ddd[k] = ''.join(i).split()


# функция честно сперта отсюда http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


result, result2 = [], []
for i in letters:
    for j in letters:
        if find_path(ddd, i, j) is not None:
            result.append(j)

for i in result:
    result2.append(f'{i} : {result.count(i)}')
for i in sorted(set(result2)):
    print(i)
