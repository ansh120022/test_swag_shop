from locators.order_confirmation import OrderConfirmationPage as p
import logging

logger = logging.getLogger("app")


class OrderConfirmationPage:
    def __init__(self, app):
        self.app = app

    def get_subheader(self):
        element = self.app.driver.find_element(*p.SUBHEADER).text
        logger.info(f"Открылась страница {element}")
        return element
