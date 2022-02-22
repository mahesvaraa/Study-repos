from time import sleep

import pytest

from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

"""
ДИСКЛЕЙМЕР!
следующие тесты по заданию у меня вызываются с названием user, но от двух классов
test_user_can_add_product_to_basket
test_guest_can_add_product_to_basket
test_guest_cant_see_product_in_basket_opened_from_product_page
test_guest_can_go_to_login_page_from_product_page

т.е в выводе они будут соответственно выглядят так:                                                                             
test_product_page.py::TestUser::test_user_can_add_product_to_basket
test_product_page.py::TestGuest::test_user_can_add_product_to_basket
test_product_page.py::TestGuest::test_user_cant_see_product_in_basket_opened_from_product_page
test_product_page.py::TestGuest::test_user_can_go_to_login_page_from_product_page  

я делал от наследования - функции реализованы один раз, но вызываются дважды, с авторизацией (как user) и без (guest)
НЕ СНИЖАЙ БАЛЛЫ ЗА ТО, ЧТО НЕ ПО ЗАДАНИЮ НАЗВАНЫ, ПОЖАЛУЙСТА <3
"""


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

    @pytest.mark.need_review
    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        if self.need_auth:
            pytest.skip('basket is not empty with auth')
        url = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
        page = BasePage(browser, url)
        login_user(page, self.need_auth)
        page.open()
        page.go_to_the_basket()
        page = BasketPage(browser, browser.current_url)
        page.check_empty_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
        page = ProductPage(browser, url)
        login_user(page, self.need_auth)
        sleep(1)
        page.open()
        page.get_product_name()
        page.add_to_basket_button()
        page.go_to_the_basket()
        page = BasketPage(browser, url)
        page.product_is_exist_in_basket()
        sleep(3)

    @pytest.mark.need_review
    def test_user_can_go_to_login_page_from_product_page(self, browser):
        if self.need_auth:
            pytest.skip('test as user no need fo review')
        url = 'https://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/'
        page = BasePage(browser, url)
        login_user(page, self.need_auth)
        sleep(1)


class TestGuest(TestUser):
    need_auth = False
