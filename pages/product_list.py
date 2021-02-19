import logging
from locators.product_list import ProductList as p

logger = logging.getLogger()


class ProductList:
    def __init__(self, app):
        self.app = app

    def add_to_cart_button(self):
        return self.app.driver.find_element(*p.ADD_TO_CART_BUTTON)

    def left_menu_button(self):
        return self.app.driver.find_element(*p.left_menu_button)

    def cart_counter(self):
        return self.app.driver.find_element(*p.cart_counter)

    def cart_link(self):
        return self.app.driver.find_element(*p.cart_link)

    def item_name(self):
        return self.app.driver.find_element(*p.item_name)

    def item_price(self):
        return self.app.driver.find_element(*p.item_price)

    def item(self):
        return self.app.driver.find_element(*p.item)

    def items_list(self):
        return self.app.driver.find_element(*p.items_list)

    def sort_name_a_z(self):
        return self.app.driver.find_element(*p.sort_name_a_z)

    def sort_name_z_a(self):
        return self.app.driver.find_element(*p.sort_name_z_a)

    def sort_price_low_high(self):
        return self.app.driver.find_element(*p.sort_price_low_high)

    def sort_price_high_low(self):
        return self.app.driver.find_element(*p.sort_price_high_low)

    def menu_dropdown(self):
        return self.app.driver.find_element(*p.menu_dropdown)

    def header(self):
        return self.app.driver.find_element(*p.header)
