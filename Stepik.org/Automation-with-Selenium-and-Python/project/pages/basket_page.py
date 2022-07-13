from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def empty_basket(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_SUMMARY)
        except NoSuchElementException:
            return True
        return False
