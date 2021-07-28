from typing import List
import pytest

from pages.product_page import ProductPage


class TestProductPage:

    links = ["http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"]

    @pytest.mark.parametrize('link', links)
    def test_guest_can_add_product_to_basket(self, browser, link: str):

        product_page = ProductPage(browser, link) 
        product_page.open()   
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.check_added_book()
