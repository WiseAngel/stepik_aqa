from selenium.webdriver.common.by import By


from .base_page import BasePage
from .locators import ProductPageLocators as PPL


class ProductPage(BasePage): 

    book_title: str
    book_in_basket: str
    book_price: str
    сost_book_in_basket: str

    def add_to_cart(self):

        btn = self.browser.find_element(*PPL.BTN_ADD_TO_BASKET)
        self.book_title = self.browser.find_element(*PPL.BOOK_TITLE).text
        self.book_price = self.browser.find_element(*PPL.PRICE).text
        btn.click()

    
    def check_added_book(self):

        self.added_selected_book()
        self.price_corresponds_to_the_book()


    def added_selected_book(self):

        self.book_in_basket = self.browser.find_element(*PPL.MESSAGE_WITH_BOOK_TITLE).text
        assert self.book_title == self.book_in_basket, f'Добавили в корзину {self.book_title}, а в корзине оказалась {self.book_in_basket}'

    
    def price_corresponds_to_the_book(self):

        self.сost_book_in_basket = self.browser.find_element(*PPL.MESSAGE_WITH_PRICE).text
        assert self.book_price == self.сost_book_in_basket, f'Стоимость выбранной книги {self.book_price}, стоимость книги в корзине {self.сost_book_in_basket}'
