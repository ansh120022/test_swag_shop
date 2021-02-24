from selenium.webdriver.support.wait import WebDriverWait
from locators.product_list import ProductList as p
from selenium.webdriver.support import expected_conditions as EC


class ProductList:
    def __init__(self, app):
        self.app = app

    def add_to_cart_button(self):
        return self.app.driver.find_element(*p.ADD_TO_CART_BUTTON)

    def left_menu_button(self):
        return self.app.driver.find_element(*p.LEFT_MENU_BUTTON)

    def cart_counter(self):
        return self.app.driver.find_element(*p.CART_COUNTER)

    def cart_link(self):
        return self.app.driver.find_element(*p.CART_LINK)

    def item_name(self):
        return self.app.driver.find_element(*p.ITEM_NAME)

    def item_price(self):
        return self.app.driver.find_element(*p.ITEM_PRICE)

    def item(self):
        return self.app.driver.find_element(*p.ITEM)

    def items_list(self):
        return self.app.driver.find_elements(*p.ITEMS_LIST)

    def sort_dropdown(self):
        return self.app.driver.find_element(*p.SORT_DROPDOWN)

    def sort_name_a_z(self):
        return self.app.driver.find_element(*p.SORT_NAME_A_Z)

    def sort_name_z_a_locator(self):
        return self.app.driver.find_element(*p.SORT_NAME_Z_A)

    def sort_price_low_high(self):
        return self.app.driver.find_element(*p.SORT_PRICE_LOW_HIGH)

    def sort_price_high_low(self):
        return self.app.driver.find_element(*p.SORT_PRICE_HIGH_LOW)

    def menu_dropdown(self):
        return self.app.driver.find_element(*p.SORT_DROPDOWN)

    def header(self):
        return self.app.driver.find_element(*p.HEADER).text

    def get_list_of_product_names(self):
        products = self.app.driver.find_elements(*p.ITEM_NAME)
        return [item.text for item in products]

    def click_sort(self):
        self.menu_dropdown().click()

    def do_sort_name_a_z(self):
        self.click_sort()
        sort_option = WebDriverWait(self.app.driver, 5).until(
            EC.presence_of_element_located(self.sort_name_a_z)
        )
        sort_option.click()

    def do_sort_name_z_a(self):
        self.click_sort()
        sort_option = WebDriverWait(self.app.driver, 5).until(
            EC.presence_of_element_located(p.SORT_NAME_Z_A)
        )
        sort_option.click()

    def do_sort_price_high_low(self):
        self.click_sort()
        sort_option = WebDriverWait(self.app.driver, 5).until(
            EC.presence_of_element_located(self.sort_price_high_low)
        )
        sort_option.click()

    def do_sort_price_low_high(self):
        self.click_sort()
        sort_option = WebDriverWait(self.app.driver, 5).until(
            EC.presence_of_element_located(self.sort_price_low_high)
        )
        sort_option.click()
