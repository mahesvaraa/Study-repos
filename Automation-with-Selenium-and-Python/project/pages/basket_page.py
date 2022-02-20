from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
from .base_page import BasePage
import math


class BasketPage(BasePage):
    def empty_basket(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_SUMMARY)
        except NoSuchElementException:
            return True
        return False
