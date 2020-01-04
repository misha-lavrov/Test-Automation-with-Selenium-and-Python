from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert ("login" in self.browser.current_url), f"'login' phrase is not present in the url: ${self.url} "

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f"login form for selector ${LoginPageLocators.LOGIN_FORM} is not exist"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), f"login form for selector ${LoginPageLocators.REGISTER_FORM} is not exist"

