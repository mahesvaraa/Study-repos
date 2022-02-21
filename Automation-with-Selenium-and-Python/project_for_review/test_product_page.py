from .pages.base_page import BasePage


class TestUserAddToBasketFromProductPage:

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer9"
        page = BasePage(browser, url)
        page.open()
        print(page.lang)

    def test_user_can_add_product_to_basket(self):
        pass

    def test_user_cant_see_product_in_basket_opened_from_product_page(self):
        pass

    def test_user_can_go_to_login_page_from_product_page(self):
        pass


class TestGuestAddToBasketFromProductPage:

    def test_user_cant_see_success_message(self):
        pass

    def test_user_can_add_product_to_basket(self):
        pass

    def test_user_cant_see_product_in_basket_opened_from_product_page(self):
        pass

    def test_user_can_go_to_login_page_from_product_page(self):
        pass
