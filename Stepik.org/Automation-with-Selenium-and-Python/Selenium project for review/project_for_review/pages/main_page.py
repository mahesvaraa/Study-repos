from .base_page import BasePage
from .basket_page import BasketPage
from .product_page import ProductPage


class MainPage(BasePage, ProductPage, BasketPage):
    pass
