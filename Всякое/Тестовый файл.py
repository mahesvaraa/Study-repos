# import unittest
#
#
# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()
#     print('Passed!')
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import warnings



class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        result = False
        message = ''
        try:

            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']").send_keys("Firstname")
            browser.find_element(By.XPATH,  "//div[@class='first_block']//input[@class='form-control second']").send_keys("Secondname")
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']").send_keys("Email")
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()
            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have su2ccessfully registered!", welcome_text, 'результат не тот')

        except Exception as err:
            result = True
            message = f"{type(err)}, {err.args[0]}"

        self.assertEqual(result, False, f"Тест не дошел до конца. {message}")
        time.sleep(2)
        browser.quit()

    def test_registration2(self):
        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)
        result = False
        message = ''
        try:

            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']").send_keys("Firstname")
            browser.find_element(By.XPATH,  "//div[@class='first_block']//input[@class='form-control second']").send_keys("Secondname")
            browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']").send_keys("Email")
            browser.find_element(By.CSS_SELECTOR, "button.btn").click()
            time.sleep(1)
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            assert "Congratulations! You have successfully registered!" == welcome_text

        except Exception as err:
            result = True
            message = f"{type(err)}, {err.args[0]}"

        self.assertEqual(result, False, f"Тест не дошел до конца. {message}")
        time.sleep(2)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
