from .base_page import BasePage
from .basket_page import BasketPage
from .locators import ProductPageLocators


class ProductPage(BasePage, BasketPage):
    def add_to_basket_button(self):
        self.should_be_add_to_basket_button()
        self.click_add_to_basket_button()

    def promo(self):
        self.check_alert_message()
        self.should_be_promo_url()

    def should_be_promo_url(self):
        assert '?promo=newYear' in self.browser.current_url, '"?promo=newYear" not in url'

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), "button 'add to basket' does not exist"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should it be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is disappeared"

    def click_add_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def check_alert_message(self):
        self.solve_quiz_and_get_code()
        result = self.browser.find_element(*ProductPageLocators.RESULT_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert result == product_name
