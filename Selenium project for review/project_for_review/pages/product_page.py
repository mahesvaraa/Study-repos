from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    product_name = ''

    def add_to_basket_button(self):
        self.should_be_add_to_basket_button()
        self.click_add_to_basket_button()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "button 'add to basket' does not exist"

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def get_product_name(self):
        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
