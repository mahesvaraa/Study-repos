from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators
from .locators import BasketPageLocators
from .base_page import BasePage
from .product_page import ProductPage


class BasketPage(BasePage):
    def empty_basket(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_SUMMARY)
            return False
        except NoSuchElementException:
            return True

    def check_empty_basket(self):
        assert self.empty_basket(), 'basket is not empty'

    def product_is_exist_in_basket(self):
        product = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert ProductPage.product_name in product, f'{ProductPage.product_name} not in basket'
