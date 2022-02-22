from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    INPUT_REG_EMAIL = (By.NAME, 'registration-email')
    INPUT_REG_PASSWORD = (By.NAME, 'registration-password1')
    INPUT_REG_PASSWORD2 = (By.NAME, 'registration-password2')
    INPUT_REG_SUBMIT = (By.NAME, 'registration_submit')
    INPUT_MESSAGE_SUCCESS = (By.CSS_SELECTOR, '#messages > div > div')
    INPUT_LOGIN = (By.NAME, 'login-username')
    INPUT_LOGIN_PASSWORD = (By.NAME, 'login-password')
    INPUT_LOGIN_SUBMIT = (By.NAME, 'login_submit')


class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    RESULT_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_NAME2 = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')


class BasketPageLocators:
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '#basket_formset')
    BASKET_SUMMARY = (By.CLASS_NAME, 'basket_summary')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET = (By.CSS_SELECTOR, 'div.basket-mini.pull-right.hidden-xs > span > a')
