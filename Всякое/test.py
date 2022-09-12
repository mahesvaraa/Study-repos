
import time

import selenium.common.exceptions as exc
import selenium.webdriver.support.expected_conditions as ec
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def is_element_appeared(driver, locator, timeout=10):
    try:
        WebDriverWait(driver,timeout,1,exc.TimeoutException).\
            until(ec.presence_of_element_located(locator))
    except exc.TimeoutException:
        return False
    return True

def send_all_checkboxes(driver):
    for i in driver.find_elements_by_css_selector('div.quiz-plugin span.s-checkbox__circle'):
        i.click()
    driver.find_element_by_css_selector('button.submit-submission').click()


USERNAME = 'anonmizer@mail.ru'  # Your login (e-mail)
PASSWORD = 'd170296'  # Your password

browser = webdriver.Chrome()
browser.implicitly_wait(10)
wait = WebDriverWait(browser, 15)

task_link = 'https://stepik.org/lesson/13240/step/7?unit=3426'

# Authorization on Stepik
browser.get('https://www.cuntempire.com/')
time.sleep(8)
actions = ActionChains(browser)
x = browser.find_element(By.CLASS_NAME, 'dirty-angels-iframe')
print(x.location)
print(x.size)
x = browser.find_element(By.ID, 'game')
print(x.location)
print(x.size)
x = 457
y = 662
time.sleep(30)
# for i in range(0, 400, 20):
#     for j in range(0, 1200, 20):
actions.move_by_offset(317, 344).click()
while True:
    actions.click().perform()

# for i in range(0,100, 1):
#     actions.move_by_offset(0, i).click()
#     print(i)
#     time.sleep(2)
#     actions.click().perform()
# elem = wait.until(ec.presence_of_element_located((By.ID, 'id_login_email')))
# elem.click()
# elem.send_keys(USERNAME)
# elem = browser.find_element_by_id('id_login_password')
# elem.click()
# elem.send_keys(PASSWORD)
# browser.find_element_by_css_selector('button.sign-form__btn').click()
# time.sleep(3)
