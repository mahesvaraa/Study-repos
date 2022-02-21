from .locators import MainPageLocators
import time
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, '"login" not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "login_form does not exist"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "register_form does not exist"

    def register(self):
        self.find_element(*LoginPageLocators.INPUT_REG_EMAIL).sendkeys(str(time.time()) + "@fakemail.org")
        self.find_element(*LoginPageLocators.INPUT_REG_PASSWORD).sendkeys('1qaz@WSX#EDC')
        self.find_element(*LoginPageLocators.INPUT_REG_PASSWORD2).sendkeys('1qaz@WSX#EDC')
        self.find_element(*LoginPageLocators.INPUT_REG_SUBMIT).click()

    def login(self):
        self.find_element(*LoginPageLocators.INPUT_LOGIN).sendkeys('12333@mail.ru')
        self.find_element(*LoginPageLocators.INPUT_LOGIN_PASSWORD).sendkeys('1qaz@WSX#EDC')
        self.find_element(*LoginPageLocators.INPUT_REG_SUBMIT).click()