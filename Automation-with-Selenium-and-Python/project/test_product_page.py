from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket_button()
    page.promo()
    time.sleep(3)


@pytest.mark.xfail(reason="is not true, message should be")
@pytest.mark.skip(reason="is not true, message should be")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer9"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket_button()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason="not working")
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket_button()
    page.should_be_disappeared_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    time.sleep(10)
    page.go_to_the_basket()
    assert page.empty_basket(), 'basket not empty'
    time.sleep(5)
