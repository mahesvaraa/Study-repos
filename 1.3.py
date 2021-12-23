import requests
import json
res = []

client_id = 'bbc8b3c2dc1ec6f120be'
client_secret = '95f5e8b95a285b47b6a54d01188a8b8e'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

# инициируем запрос с заголовком
for i in range(15):
    line = input()
    ln = r"https://api.artsy.net/api/artists/"+line.strip()+"/"
    #print(ln)
    r = requests.get(f"{ln}", headers=headers)
    # разбираем ответ сервера
    j = json.loads(r.text)
    res.append((j['sortable_name'],j['birthday']))
for i in sorted(res, key = lambda x: x[1]):
    print(i[0])
