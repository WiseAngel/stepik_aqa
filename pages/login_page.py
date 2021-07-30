from .base_page import BasePage
from .locators import LoginPageLocators as LPL


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.go_to_login_page()
        email_field = self.browser.find_element(
            *LPL.REGISTATION_EMAIL).send_keys(f'{email}')
        password_field = self.browser.find_element(
            *LPL.REGISTATION_PASSWORD).send_keys(f'{password}')
        password_confirm_field = self.browser.find_element(
            *LPL.REGISTATION_PASSWORD_CONFIRM).send_keys(f'{password}')
        btn_confirm = self.browser.find_element(*LPL.BTN_REGISTRATION).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert url.find('login') != -1, f'Substring not found! URL {url}'

    def should_be_login_form(self):
        assert self.is_element_present(
            *LPL.LOGIN_FORM), 'Login form is not presented'
        assert self.is_element_present(
            *LPL.LOGIN_EMAIL), 'Email field is not presented'
        assert self.is_element_present(
            *LPL.LOGIN_PASSWORD), 'Password field is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LPL.REGISTATION_FORM), 'Registrtion form is not presented'
        assert self.is_element_present(
            *LPL.REGISTATION_EMAIL), 'Email field is not presented'
        assert self.is_element_present(
            *LPL.REGISTATION_PASSWORD), 'Password field is not presented'
        assert self.is_element_present(
            *LPL.REGISTATION_PASSWORD_CONFIRM), 'Password confirm fiel is not presented'
        
    def should_be_successful_registration(self):
        assert self.is_element_present(*LPL.SUCCESSFUL_REGISTRATION_MESSAGE), 'Successful message not found'
