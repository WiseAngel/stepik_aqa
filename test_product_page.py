import pytest

from pages.product_page import ProductPage


class TestProductPage:

    links = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207?promo=offer0']

    skipped_links = [
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7']


    def _init_(self, browser, link: str):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_cart()
        return product_page
        

    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('link', [pytest.param(*skipped_links, marks=pytest.mark.xfail), *links])
    def test_guest_can_add_product_to_basket(self, browser, link: str):

        pp = self._init_(browser, link)
        pp.solve_quiz_and_get_code()
        pp.check_added_book()
    

    @pytest.mark.parametrize('link', links)
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link: str): 
        
        pp = self._init_(browser, link)
        pp.solve_quiz_and_get_code()
        pp.should_not_be_success_message()
    

    @pytest.mark.parametrize('link', links)
    def test_guest_cant_see_success_message(self, browser, link: str): 
        
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()


    @pytest.mark.parametrize('link', links)
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link: str): 
       
        pp = self._init_(browser, link)
        pp.solve_quiz_and_get_code()
        pp.success_message_is_disappeared()

