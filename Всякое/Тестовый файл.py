from selenium.webdriver.common.by import By
from time import sleep


def test_guest_should_see_login_link(browser, language):
    browser.get(language)
    sleep(2)
    browser.find_element(By.CLASS_NAME, 'btn-add-to-basket').click()
    sleep(2)
    result = browser.find_element(By.XPATH, '//*[@id="messages"]/div[1]/div/strong').text
    product_name = browser.find_element(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1').text
    assert result == product_name
    print(f'Проверка наличия кнопки "добавить в корзину" и ее нажатия на товаре {product_name}')
