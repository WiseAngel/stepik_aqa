import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

links = [
    # 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207']


# @pytest.mark.skip(reason="no way of currently testing this")
@pytest.mark.parametrize('link', links)
class TestProductPage():

    def _init_(self, browser, link: str):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_cart()
        return product_page

    # @pytest.mark.skip(reason="no way of currently testing this")
    # @pytest.mark.parametrize('link', [pytest.param(*skipped_links, marks=pytest.mark.xfail), *links])
    def test_guest_can_add_product_to_basket(self, browser, link: str):
        pp = self._init_(browser, link)
        pp.check_added_book()

    # @pytest.mark.skip(reason="no way of currently testing this")
    # @pytest.mark.parametrize('link', links)
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link: str):
        pp = self._init_(browser, link)
        pp.should_not_be_success_message()

    # @pytest.mark.skip(reason="no way of currently testing this")
    # @pytest.mark.parametrize('link', links)
    def test_guest_cant_see_success_message(self, browser, link: str):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    # @pytest.mark.skip(reason="no way of currently testing this")
    # @pytest.mark.parametrize('link', links)
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser, link: str):
        pp = self._init_(browser, link)
        pp.success_message_is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser, link: str):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser, link: str):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser, link: str):
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket()
        page.basket_should_be_empty()
