import time
import math
from selenium import webdriver

link = 'http://suninjuly.github.io/math.html'

# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
# with webdriver.Chrome() as browser:
#     browser.get(link)

#     x = browser.find_element_by_id('input_value').text

#     res = calc(x)

#     textarea = browser.find_element_by_id('answer')
#     textarea.send_keys(res)

#     checkbox = browser.find_element_by_id('robotCheckbox')
#     checkbox.click()

#     radiobuton = browser.find_element_by_id('robotsRule')
#     radiobuton.click()

#     btn = browser.find_element_by_css_selector('.btn.btn-default')
#     btn.click()

#     time.sleep(5)


class PassCaptcha:

    def __init__(self, link: str) -> None:
        self.link = link

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        return self

    def __calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))

    def pass_captcha(self):
        browser = webdriver.Chrome()
        browser.get(self.link)

        x = browser.find_element_by_id('input_value').text

        res = self.__calc(x)

        textarea = browser.find_element_by_id('answer')
        textarea.send_keys(res)

        checkbox = browser.find_element_by_id('robotCheckbox')
        checkbox.click()

        radiobuton = browser.find_element_by_id('robotsRule')
        radiobuton.click()

        btn = browser.find_element_by_css_selector('.btn.btn-default')
        btn.click()

        time.sleep(1)


with PassCaptcha(link) as tc:
    tc.pass_captcha()
