from locators.cart_icon import CartIcon as e
import logging

logger = logging.getLogger("app")


class CartIconElement:
    def __init__(self, app):
        self.app = app

    def get_cart_counter(self):
        """Значение счётчика на корзине"""
        counter_value = 0
        not_empty = len(self.app.driver.find_elements(*e.CART_COUNTER)) > 0
        if not_empty:
            counter_value = int(self.app.driver.find_element(*e.CART_COUNTER).text)
        logger.info(f"Число товаров в корзине: {counter_value}")
        return counter_value

    def cart_icon(self):
        return self.app.driver.find_element(*e.CART_LINK)

    def click_cart(self):
        logger.info("Переход в корзину")
        self.cart_icon().click()
