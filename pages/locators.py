from selenium.webdriver.common.by import By


class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")


class MainPageLocators():
    pass


class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    BTN_SUBMIT = (By.CSS_SELECTOR, "#register_form > button")

    REGISTATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTATION_PASSWORD_CONFIRM = (
        By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REGISTRATION = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert .alertinner')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BOOK_TITLE = (By.CSS_SELECTOR, '.product_main > h1')
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGE_WITH_BOOK_TITLE = (
        By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    MESSAGE_WITH_PRICE = (
        By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
