import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def send_answer(answer, link):
    # в функцию передаем ответ и ссылку текущего урока

    browser = webdriver.Chrome()

    email = 'danilashkirdov.itv@gmail.com'  # ваша почта на степике
    password = 'Dd170296d'  # ваш пароль

    browser.get(link)
    time.sleep(5)

    current_url = str(browser.current_url)
    if 'promo' in current_url:
        browser.get(current_url + '?auth=login')
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, '[name = "login"]').send_keys(email)
        browser.find_element(By.CSS_SELECTOR, '[name = "password"]').send_keys(password)
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
        time.sleep(1)

    browser.get(link)
    time.sleep(5)
    right = browser.find_element(By.CSS_SELECTOR, 'div[data-type="string-quiz"]').get_attribute('data-state')
    if right == 'no_submission':
        browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]').clear()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
    else:
        browser.find_element(By.CSS_SELECTOR, 'button[class="again-btn white"]').click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'footer[class="modal-popup__footer ember-view"] :first-child').click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]').clear()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]').send_keys(answer)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, 'button[class ="submit-submission"]').click()

def sendd(answer, link):
    send = input(f'Отослать ответ: {answer}? Y/N')
    if send in ['Y', 'y', 'Н', 'н']: send_answer(answer, link)