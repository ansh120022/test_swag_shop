from locators.auth import Login as p
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging

logger = logging.getLogger("app")


class LoginPage:
    def __init__(self, app):
        self.app = app

    def username_field(self):
        return self.app.driver.find_element(*p.USERNAME_INPUT)

    def password_field(self):
        return self.app.driver.find_element(*p.PASSWORD_INPUT)

    def submit_button(self):
        return self.app.driver.find_element(*p.LOGIN_SUBMIT)

    def error_icon(self):
        return self.app.driver.find_elements(*p.ERROR_ICON)

    def error_text(self):
        return self.app.driver.find_element(*p.ERROR_TEXT)

    def get_error_text(self):
        WebDriverWait(self.app.driver, 5).until(
            EC.presence_of_element_located(p.ERROR_TEXT)
        )
        return self.error_text().text

    def do_login(self, login, passwd):
        logger.info(f"Вход с логином {login} и паролем {passwd}")
        self.username_field().send_keys(login)
        self.password_field().send_keys(passwd)
        self.submit_button().click()
