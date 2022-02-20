from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    RESULT_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, 'a[href="/ru/accounts/login/"]')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
