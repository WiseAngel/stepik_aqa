from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage): 

    def go_to_login_page(self):
        # assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()
        
        

    def should_be_login_link(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"



    
