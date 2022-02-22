import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '"login" not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login_form does not exist"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register_form does not exist"

    def register(self):
        self.browser.find_element(*LoginPageLocators.INPUT_REG_EMAIL).send_keys(str(time.time()) + "@fakemail.org")
        self.browser.find_element(*LoginPageLocators.INPUT_REG_PASSWORD).send_keys('1qaz@WSX#EDC')
        self.browser.find_element(*LoginPageLocators.INPUT_REG_PASSWORD2).send_keys('1qaz@WSX#EDC')
        self.browser.find_element(*LoginPageLocators.INPUT_REG_SUBMIT).click()
        assert self.is_element_present(*LoginPageLocators.INPUT_MESSAGE_SUCCESS), 'Not Register'

    def login(self):
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN).send_keys('12333@mail.ru')
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN_PASSWORD).send_keys('1qaz@WSX#EDC')
        self.browser.find_element(*LoginPageLocators.INPUT_LOGIN_SUBMIT).click()
        assert self.is_element_present(*LoginPageLocators.INPUT_MESSAGE_SUCCESS), 'Not Login'

