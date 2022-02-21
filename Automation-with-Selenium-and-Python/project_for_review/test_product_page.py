from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from time import sleep
import pytest


def registration_user(page, need_auth=False):
    if need_auth:
        page.open()
        page.go_to_login_page()
        LoginPage.register(page)


def login_user(page, need_auth=False):
    if need_auth:
        page.open()
        page.go_to_login_page()
        LoginPage.login(page)


class TestUser:
    need_auth = True

    @pytest.mark.skipif(__name__ == 'TestUser', reason ='User')
    def test_user_cant_see_success_message_with_registration(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer9"
        page = BasePage(browser, url)
        registration_user(page, self.need_auth)
        page.open()
        sleep(3)

    def test_user_cant_see_success_message_with_login(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer9"
        page = BasePage(browser, url)
        login_user(page, self.need_auth)
        page.open()
        sleep(3)

    def test_user_can_add_product_to_basket(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/'
        page = BasePage(browser, url)
        page.open()
        page.go_to_the_basket()
        sleep(3)
        pass

    def test_user_cant_see_product_in_basket_opened_from_product_page(self):
        pass

    def test_user_can_go_to_login_page_from_product_page(self):
        pass


class TestGuest(TestUser):
    need_auth = False
    pass
