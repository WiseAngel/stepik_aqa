import time
import math
from selenium import webdriver

link = 'http://suninjuly.github.io/alert_accept.html'

class ConfirmAlert:

    def __init__(self, link: str) -> None:
        self.link = link

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        return self

    def __calc(self, x):
        return str(math.log(abs(12*math.sin(int(x)))))

    def conf_alert(self):
        browser = webdriver.Chrome()
        browser.get(self.link)

        btn = browser.find_element_by_css_selector('.btn.btn-primary')
        btn.click()

        alert = browser.switch_to.alert
        alert.accept()

        x = browser.find_element_by_id('input_value').text

        res = self.__calc(x)

        textarea = browser.find_element_by_id('answer')
        textarea.send_keys(res)

        btn_submit = browser.find_element_by_css_selector('.btn.btn-primary')
        btn_submit.click()

        time.sleep(10)


with ConfirmAlert(link) as ca:
    try:
        ca.conf_alert()
    except Exception as err:
        print(err)

