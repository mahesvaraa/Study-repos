from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "input_value")
    summ = calc(num1.text)
    input = browser.find_element(By.ID, "answer").send_keys(summ)

    checkbox = browser.find_element_by_css_selector('[id="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radiobtn = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
    radiobtn.click()

    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()