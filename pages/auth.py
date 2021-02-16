import logging
from locators.auth import Login

logger = logging.getLogger()


class LoginPage:
    def __init__(self, app):
        self.app = app

    def username_field(self):
        return self.app.driver.find_element(*Login.USERNAME_INPUT)

    def password_field(self):
        return self.app.driver.find_element(*Login.PASSWORD_INPUT)

    def submit_button(self):
        return self.app.driver.find_element(*Login.LOGIN_SUBMIT)

    def error_icon(self):
        return self.app.driver.find_elements(*Login.ERROR_ICON)

    def do_login(self):
        self.username_field().send_keys("standard_user")
        self.password_field().send_keys("secret_sauce")
        self.submit_button().click()
