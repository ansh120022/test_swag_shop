from locators.cart import CartPage as p


class CartPage:
    def __init__(self, app):
        self.app = app

    def continue_shopping_button(self):
        return self.app.driver.find_element(*p.CONTINUE_SHOPPING_BUTTON)

    def checkout_button(self):
        return self.app.driver.find_element(*p.CHECKOUT_BUTTON)

    def item_price(self):
        return self.app.driver.find_element(*p.ITEM_PRICE)

    def remove_button(self):
        return self.app.driver.find_element(*p.REMOVE_BUTTON)

    def subheader(self):
        return self.app.driver.find_element(*p.SUBHEADER).text

    def click_continue_shopping(self):
        self.continue_shopping_button().click()

    def click_checkout(self):
        self.checkout_button().click()

    def remove_all_from_cart(self):
        remove_buttons = self.app.driver.find_elements(*p.REMOVE_BUTTON)
        while remove_buttons:
            remove = self.app.driver.find_element(*p.REMOVE_BUTTON)
            remove.click()
            remove_buttons = self.app.driver.find_elements(*p.REMOVE_BUTTON)

    def get_sum_prices(self):
        """Рассчёт суммы товаров в корзине"""
        price_elements = self.app.driver.find_elements(*p.ITEM_PRICE)
        total = 0.0
        for price in price_elements:
            total += float(price.text)
        return total
