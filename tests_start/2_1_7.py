import math
import time

from selenium import webdriver

link = 'http://suninjuly.github.io/get_attribute.html'

# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
# with webdriver.Chrome() as browser:
#     browser.get(link)

#     picx = browser.find_element_by_id('treasure')
#     x = picx.get_attribute('valuex')
#     print(x)

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


class Captcha:

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

        picx = browser.find_element_by_id('treasure')
        x = picx.get_attribute('valuex')
        print(x)

        res = self.__calc(x)

        textarea = browser.find_element_by_id('answer')
        textarea.send_keys(res)

        checkbox = browser.find_element_by_id('robotCheckbox')
        checkbox.click()

        radiobuton = browser.find_element_by_id('robotsRule')
        radiobuton.click()

        btn = browser.find_element_by_css_selector('.btn.btn-default')
        btn.click()

        time.sleep(5)


with Captcha(link) as tc:
    try:
        tc.pass_captcha()
    except Exception as err:
        print(err)
