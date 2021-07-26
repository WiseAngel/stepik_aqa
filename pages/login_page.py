from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from .locators import LoginPageLocators as LPL


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find('login') != -1, f'Подсктрока не найдена! URL {url}'

    def should_be_login_form(self):
        assert self.is_element_present(*LPL.LOGIN_FORM), 'Область формы логина не найдена'
        assert self.is_element_present(*LPL.LOGIN_EMAIL), 'Поле Логин.Емайл не найдено'
        assert self.is_element_present(*LPL.LOGIN_PASSWORD), 'Поле Логин.Пассворд не найдено'
        # assert self.browser.find_element(*LPL.LOGIN_FORM).is_displayed(), 'Область формы логина не найдена'
        # assert WW(self.browser, 5).until(EC.element_to_be_clickable([*LPL.LOGIN_EMAIL])).is_displayed(), 'Поле Логин.Емайл не найдено'
        # assert WW(self.browser, 5).until(EC.element_to_be_clickable([*LPL.LOGIN_PASSWORD])).is_displayed(), 'Поле Логин.Пассворд не найдено'


    def should_be_register_form(self):
        assert self.is_element_present(*LPL.REGISTATION_FORM), 'Область формы реги не найдена'
        assert self.is_element_present(*LPL.REGISTATION_EMAIL), 'Поле Рег.Емайл не найдено'
        assert self.is_element_present(*LPL.REGISTATION_PASSWORD), 'Поле Рег.Пасс1 не найдено'
        assert self.is_element_present(*LPL.REGISTATION_PASSWORD_CONFIRM), 'Поле Рег.Пасс2 не найдено'
        # assert self.browser.find_element(*LPL.REGISTATION_FORM).is_displayed(), 'Область формы реги не найдена'
        # assert WW(self.browser, 2).until(EC.element_to_be_clickable([*LPL.REGISTATION_EMAIL])).is_displayed(), 'Поле Рег.Емайл не найдено'
        # assert WW(self.browser, 2).until(EC.element_to_be_clickable([*LPL.REGISTATION_PASSWORD])).is_displayed(), 'Поле Рег.Пасс1 не найдено'
        # assert WW(self.browser, 2).until(EC.element_to_be_clickable([*LPL.REGISTATION_PASSWORD_CONFIRM])), 'Поле Рег.Пасс2 не найдено'