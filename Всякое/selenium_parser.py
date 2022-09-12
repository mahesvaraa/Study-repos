
import time

import selenium.common.exceptions as exc
import selenium.webdriver.support.expected_conditions as ec
from selenium import webdriver
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


USERNAME = ''  # Your login (e-mail)
PASSWORD = ''  # Your password

browser = webdriver.Chrome()
browser.implicitly_wait(10)
wait = WebDriverWait(browser, 15)

task_link = 'https://stepik.org/lesson/13240/step/7?unit=3426'

# Authorization on Stepik
browser.get('https://stepik.org/catalog?auth=login')
elem = wait.until(ec.presence_of_element_located((By.ID, 'id_login_email')))
elem.click()
elem.send_keys(USERNAME)
elem = browser.find_element_by_id('id_login_password')
elem.click()
elem.send_keys(PASSWORD)
browser.find_element_by_css_selector('button.sign-form__btn').click()
time.sleep(3)

# Go get them, Tiger!
browser.get(task_link)
is_element_appeared(browser, (By.CSS_SELECTOR, 'div.attempt'))
send_all_checkboxes(browser)
tries_amount = 10
while tries_amount and is_element_appeared(browser, (By.CSS_SELECTOR, 'span.attempt-message_wrong')):
    browser.find_element_by_css_selector('button.success').click()
    if is_element_appeared(browser,(By.CSS_SELECTOR, 'div.attempt-wrapper.no_submission.choice')):
        send_all_checkboxes(browser)
        tries_amount -= 1
    else:
        break

browser.quit()