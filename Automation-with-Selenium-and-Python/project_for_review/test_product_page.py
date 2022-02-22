from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from time import sleep
import pytest


def registration_user(page, need_auth=False):
    if need_auth:
        page.open()
        page.go_to_login_page()
        page = LoginPage(page.browser, page.browser.current_url)
        page.register()


def login_user(page, need_auth=False):
    if need_auth:
        page.open()
        page.go_to_login_page()
        page = LoginPage(page.browser, page.browser.current_url)
        page.login()


class TestUser:
    need_auth = True

    def test_user_cant_see_success_message_with_registration(self, browser):
        if not self.need_auth:
            pytest.skip('register not need for guest')
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
        url = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
        page = ProductPage(browser, url)
        page.open()
        page.get_product_name()
        page.add_to_basket_button()
        page.go_to_the_basket()
        page = BasketPage(browser, url)
        page.product_is_exist_in_basket()
        sleep(3)

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
        page = BasePage(browser, url)
        page.open()
        page.go_to_the_basket()
        page = BasketPage(browser, browser.current_url)
        page.check_empty_basket()
        sleep(3)

    def test_user_can_go_to_login_page_from_product_page(self, browser):
        pass


class TestGuest(TestUser):
    need_auth = False
