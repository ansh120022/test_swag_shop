from locators.product import ProductPage as p
import logging

logger = logging.getLogger("app")


class ProductPage:
    def __init__(self, app):
        self.app = app

    def get_price(self):
        element = self.app.driver.find_element(*p.PRICE)
        return element.text

    def get_product_name(self):
        element = self.app.driver.find_element(*p.PRODUCT_NAME)
        return element.text

    def click_add_to_cart(self):
        self.app.driver.find_element(*p.ADD_TO_CART).click()
        logger.info("Выполнено добавление в корзину")

    def remove_from_cart(self):
        self.app.driver.find_element(*p.ADD_TO_CART).click()
        logger.info("Выполнено удаление из корзины")

    def click_back(self):
        self.app.driver.find_element(*p.BACK_BUTTON).click()
        logger.info("Выполнен переход обратно")
