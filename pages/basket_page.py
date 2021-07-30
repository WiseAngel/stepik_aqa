from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import BasketPageLocators as BasketPL


class BasketPage(BasePage):
    
    def basket_should_be_empty(self):
        self.should_be_message_of_empty_basket()
        self.message_of_empty_basket_is_not_disappeared()
        self.should_not_be_basket_items()
    
    def should_be_message_of_empty_basket(self):
        assert self.is_element_present(*BasketPL.EMPTY_BASKET_MESSAGE), 'No message of empty basket'

    def message_of_empty_basket_is_not_disappeared(self):
        assert not self.is_disappeared(
            *BasketPL.EMPTY_BASKET_MESSAGE), 'Message of empty basket is disappeared'

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(
            *BasketPL.BASKET_ITEMS), 'Basket items is presented, but should not be'
