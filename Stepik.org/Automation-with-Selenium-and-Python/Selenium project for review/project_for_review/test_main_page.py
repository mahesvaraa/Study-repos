from time import sleep

import pytest

from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


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

    def test_user_cant_see_success_message_with_registration(self, browser):
        if not self.need_auth:
            pytest.skip('register not need for guest')
        url = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, url)
        registration_user(page, self.need_auth)
        page.open()
        sleep(3)

    def test_user_cant_see_success_message_with_login(self, browser):
        url = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, url)
        login_user(page, self.need_auth)
        page.open()
        sleep(3)

    @pytest.mark.xfail(reason='this is not product page')
    def test_user_can_add_product_to_basket(self, browser):
        url = 'https://selenium1py.pythonanywhere.com'
        page = ProductPage(browser, url)
        login_user(page, self.need_auth)
        page.open()
        page.get_product_name()
        page.add_to_basket_button()
        page.go_to_the_basket()
        page = BasketPage(browser, url)
        page.product_is_exist_in_basket()
        sleep(3)

    @pytest.mark.xfail(reason='this is not product page')
    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        url = 'https://selenium1py.pythonanywhere.com'
        page = BasePage(browser, url)
        login_user(page, self.need_auth)
        page.open()
        page.go_to_the_basket()
        page = BasketPage(browser, browser.current_url)
        page.check_empty_basket()
        sleep(3)

    def test_user_can_go_to_login_page_from_product_page(self, browser):
        login_user(page, self.need_auth)
        pass


class TestGuest(TestUser):
    need_auth = False
