import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW

link = 'http://suninjuly.github.io/explicit_wait2.html'

class Wait:

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

        
        WW(browser, 10).until(EC.text_to_be_present_in_element( (By.ID, "price"), '$100' ))

        btn = browser.find_element_by_css_selector('.btn.btn-primary')
        btn.click()

        x = browser.find_element_by_id('input_value').text

        res = self.__calc(x)

        textarea = browser.find_element_by_id('answer')
        textarea.send_keys(res)

        btn_submit = browser.find_elements_by_css_selector('.btn.btn-primary')[1]
        btn_submit.click()

        result = (browser.switch_to.alert).text.split(' ')[-1]
        print(result)

        time.sleep(5)


with Wait(link) as nw:
    try:
        nw.pass_captcha()
    except Exception as err:
        print(err)

