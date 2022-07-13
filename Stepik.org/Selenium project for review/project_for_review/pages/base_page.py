import math

from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.lang = ''

    # открытие страницы
    def open(self):
        self.browser.get(self.url)
        self.lang = self.browser.current_url.split('/')[3]

    # элемент присутствует
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            return True
        except NoSuchElementException:
            return False

    # элемент исчезает
    def is_disappeared(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
            return True
        except TimeoutException:
            return False

    # элемент не появился за 4 сек
    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            return False
        except TimeoutException:
            return True

    # переход на страницу логина
    def go_to_login_page(self):
        if self.should_be_login_link():
            link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
            link.click()
        else:
            return False

    # переход в корзину
    def go_to_the_basket(self):
        self.browser.find_element(*BasePageLocators.OPEN_BASKET).click()

    # должна быть кнопка авторизации
    def should_be_login_link(self):
        return self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    # решалка для промокода
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
