import logging
from locators.auth import Login
from common.constants import User as u

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

    def error_text(self):
        return self.app.driver.find_element(*Login.ERROR_TEXT)

    def get_error_text(self):
        return self.error_text().text

    def do_login_standart(self):
        self.username_field().send_keys(u.standard_user)
        self.password_field().send_keys(u.passwd)
        self.submit_button().click()

    def do_login_locked(self):
        self.username_field().send_keys(u.locked_out_user)
        self.password_field().send_keys(u.passwd)
        self.submit_button().click()

    def do_login_problem(self):
        self.username_field().send_keys(u.problem_user)
        self.password_field().send_keys(u.passwd)
        self.submit_button().click()

    def do_login_performance(self):
        self.username_field().send_keys(u.performance_user)
        self.password_field().send_keys(u.passwd)
        self.submit_button().click()

    def do_login_nonexistent(self):
        self.username_field().send_keys(u.any_str)
        self.password_field().send_keys(u.passwd)
        self.submit_button().click()

    def do_login_wrong_pass(self):
        self.username_field().send_keys(u.standard_user)
        self.password_field().send_keys(u.any_str)
        self.submit_button().click()
