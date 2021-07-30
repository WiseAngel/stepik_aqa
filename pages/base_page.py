# from selenium.common.exceptions import NoSuchElementException
import math

from selenium.common.exceptions import (NoAlertPresentException,
                                        TimeoutException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from .locators import BasePageLocators as BPL


class BasePage():

    def __init__(self, browser, url, timeout=1):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket(self):
        link = self.browser.find_element(*BPL.BASKET_LINK)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BPL.LOGIN_LINK)
        link.click()

    def is_disappeared(self, how, what, timeout=4):
        try:
            WW(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except Exception as ex:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WW(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_authorized_user(self):
        assert self.is_element_present(*BPL.USER_ICON), "User icon is not presented, probably unauthorised user"
        assert self.is_element_present(*BPL.LOGOUT_LINK), 'Logout linl is not presented, probably unauthorised user'

    def should_be_login_link(self):
        assert self.is_element_present(
            *BPL.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def open(self):
        self.browser.get(self.url)

    def quit(self):
        self.browser.quit()
