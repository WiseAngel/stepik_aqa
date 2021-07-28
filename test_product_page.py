from typing import List
import pytest

from pages.product_page import ProductPage


class TestProductPage:

    links_promo = ['http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear',
             'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019']

    links = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
              'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9']

    @pytest.mark.parametrize('link', links)
    def test_guest_can_add_product_to_basket(self, browser, link: str):

        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_cart()
        product_page.solve_quiz_and_get_code()
        product_page.check_added_book()
