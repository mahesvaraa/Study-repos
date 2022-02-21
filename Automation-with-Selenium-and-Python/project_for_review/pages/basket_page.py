from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def empty_basket(self):
        try:
            self.browser.find_element(*BasePageLocators.BASKET_SUMMARY)

        except NoSuchElementException:
            return True
        return False
