import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_add_to_cart(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element_by_css_selector('#add_to_basket_form > button').is_displayed(), 'Кнопка добавления товара в корзину отсутсвует'
    