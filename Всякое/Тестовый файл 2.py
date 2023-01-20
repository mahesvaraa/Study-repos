import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

for d in range(0):
    url = fr'https://stepik.org/lesson/{d}'
    page = requests.get(url)
    if page.status_code == 200:
        print(url)
    # print(page.status_code)
    # soup = BeautifulSoup(page, 'html.parser')
    # print(soup.find_all('div'))

url2 = r'https://stepik.org/lesson/9173/'
browser = webdriver.Chrome()
browser.implicitly_wait(10)
wait = WebDriverWait(browser, 15)
browser.get(url2)
# print(browser.page_source)
print(browser.find_element_by_tag_name("html").get_attribute("innerHTML"))
