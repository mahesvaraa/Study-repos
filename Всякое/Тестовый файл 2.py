import json
import time

import requests
from bs4 import BeautifulSoup


def stepik_parser_kursi_loop():
    start = int(input('Введите начальное число: '))  # начальное число в адресе, с которого будем начинать парсинг
    number = int(input('Введите конечное число: '))  # конечное число в адресе, с которого будем начинать парсинг
    with open('stepik.json', 'w', encoding='utf-8') as text_file:
        res = []
        for i in range(start, number + 1):
            url = 'https://stepik.org/course/' + str(i) + '/promo'
            hdr = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=hdr)
            soup = BeautifulSoup(r.text, 'lxml')
            title = soup.find('h1', attrs={'class': 'course-promo__header'})
            leaners = soup.find('div', attrs={'class': 'course-promo-summary__students'})
            print(res)
            if title is not None and leaners is not None:

                d = {'url': url, 'title': title.get_text(), 'learners': leaners.get_text().strip()}
                if 'Python' in title:
                    res.append(d)

                time.sleep(1)
            if i % 100 == 0:
                print(i)  # смотрим, сколько урлов уже прошло, выводится число кратное 100
        json.dump(res, text_file, indent=3, ensure_ascii=False)
        return True


stepik_parser_kursi_loop()
