import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from send_answer_to_stepik import send_answer, sendd

def calc(x):
    import math
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver

    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = browser.find_element(By.ID, 'book')
    textt = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button.click()
    num = browser.find_element(By.ID, "input_value").text
    input_area = browser.find_element(By.ID, "answer").send_keys(calc(num))
    submit_button = browser.find_element(By.ID, "solve").click()
    print(browser.switch_to.alert.text.split()[-1])
finally:
    #если что-то пошло не так можно отменить отправку
    time.sleep(5)
    browser.quit()