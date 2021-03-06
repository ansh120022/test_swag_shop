from locators.checkout import CheckoutPage as p
import logging

logger = logging.getLogger("app")


class CheckoutPage:
    def __init__(self, app):
        self.app = app

    def input_first_name(self, name):
        self.app.driver.find_element(*p.FIRSTNAME_TEXTBOX).send_keys(name)

    def input_last_name(self, name):
        self.app.driver.find_element(*p.LASTNAME_TEXTBOX).send_keys(name)

    def input_postal_code(self, postal_code):
        self.app.driver.find_element(*p.POSTALCODE_TEXTBOX).send_keys(postal_code)

    def fill_form(self, firstname, lastname, postalcode):
        self.input_first_name(firstname)
        self.input_last_name(lastname)
        self.input_postal_code(postalcode)
        logger.info(
            "Форма заполнена данными покупателя"
            f" Имя: {firstname}"
            f" Фамилия: {lastname}"
            f" Почтовый индекс: {postalcode}"
        )

    def get_first_name(self):
        element = self.app.driver.find_element(*p.FIRSTNAME_TEXTBOX)
        return element.get_attribute("value")

    def get_last_name(self):
        element = self.app.driver.find_element(*p.LASTNAME_TEXTBOX)
        return element.get_attribute("value")

    def get_postal_code(self):
        element = self.app.driver.find_element(*p.POSTALCODE_TEXTBOX)
        return element.get_attribute("value")

    def is_error_message_present(self):
        error_message = self.app.driver.find_elements(*p.ERROR_MESSAGE)
        return len(error_message) > 0

    def click_cancel(self):
        logger.info("Переход обратно в каталог")
        self.app.driver.find_element(*p.CANCEL_BUTTON).click()

    def click_continue(self):
        logger.info("Переход к оформлению заказа")
        self.app.driver.find_element(*p.CONTINUE_BUTTON).click()

    def get_subheader(self):
        element = self.app.driver.find_element(*p.SUBHEADER)
        return element.text
