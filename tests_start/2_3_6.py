import time
import math
from selenium import webdriver

link = 'http://suninjuly.github.io/redirect_accept.html'

class NewWindow:

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

        btn = browser.find_element_by_css_selector('.trollface')
        btn.click()

        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        x = browser.find_element_by_id('input_value').text

        res = self.__calc(x)

        textarea = browser.find_element_by_id('answer')
        textarea.send_keys(res)

        btn_submit = browser.find_element_by_css_selector('.btn.btn-primary')
        btn_submit.click()

        result = (browser.switch_to.alert).text.split(' ')[-1]
        print(result)

        time.sleep(5)


with NewWindow(link) as nw:
    try:
        nw.pass_captcha()
    except Exception as err:
        print(err)

