from selenium import webdriver
import time
import unittest

link = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'


class TestReg(unittest.TestCase):
    # def __init__(self, link: str) -> None:
    #     self.link = 'http://suninjuly.github.io/registration1.html'

    # def __enter__(self) -> None:
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb) -> None:
    #     return self


    def test_pass_captcha(self):
        browser = webdriver.Chrome()
        browser.get(link2)


        first_name = browser.find_element_by_css_selector('.first_block > .form-group.first_class > input')
        first_name.send_keys('Ivan')
        last_name = browser.find_element_by_css_selector('.first_block > .form-group.second_class > input')
        last_name.send_keys('Ivanov')
        email = browser.find_element_by_css_selector('.first_block > .form-group.third_class > input')
        email.send_keys('Ivan@ivanov.iv')
        phone = browser.find_element_by_css_selector('.second_block > .first_class > input')
        phone.send_keys('147852369')
        address = browser.find_element_by_css_selector('.second_block > .second_class > input')
        address.send_keys('Ivanovka')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector('button.btn')
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name('h1')
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual ('Congratulations! You have successfully registered!', welcome_text)

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)


# with TestReg(link) as nw:
#     try:
#         nw.test_pass_captcha()
#     except Exception as err:
#         print(err)

# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
        
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

if __name__ == "__main__":
    unittest.main()
