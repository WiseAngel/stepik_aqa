import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'

class Selects:

    def __init__(self, link: str) -> None:
        self.link = link

    def __enter__(self) -> None:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        return self

    def choose_from_list(self):
        browser = webdriver.Chrome()
        browser.get(self.link)
        
        num1 = browser.find_element_by_id('num1').text
        num2 = browser.find_element_by_id('num2').text
        res = int(num1) + int(num2)

        select = Select(browser.find_element_by_id('dropdown'))
        select.select_by_value(str(res))

        btn = browser.find_element_by_css_selector('.btn.btn-default')
        btn.click()

        time.sleep(10)


with Selects(link) as s:
    try:
       s.choose_from_list()
    except Exception as err:
        print(err)
