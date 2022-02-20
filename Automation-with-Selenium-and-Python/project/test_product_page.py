from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.locators import MainPageLocators
import time
import pytest

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def go_to_login_page(browser):
    login_link = browser.find_element(*MainPageLocators.LOGIN_LINK)
    login_link.click()


# @pytest.mark.parametrize('link', [f"{url}/?promo=offer0",
#                                   f"{url}//?promo=offer1",
#                                   f"{url}//?promo=offer2",
#                                   f"{url}//?promo=offer3",
#                                   f"{url}//?promo=offer4",
#                                   f"{url}//?promo=offer5",
#                                   f"{url}//?promo=offer6",
#                      pytest.param(f"{url}//?promo=offer7", marks=pytest.mark.xfail),
#                                   f"{url}//?promo=offer8",
#                                   f"{url}//?promo=offer9"])
@pytest.mark.xfail(reason="link without promo")
def test_product_page(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket_button()
    time.sleep(3)


@pytest.mark.xfail(reason="is not true, message should be")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="not working")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket_button()
    page.should_be_disappeared_message()
