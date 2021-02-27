from locators.order_confirmation import OrderConfirmationPage as p


class OrderConfirmationPage:
    def __init__(self, app):
        self.app = app

    def subheader(self):
        element = self.app.driver.find_element(*p.SUBHEADER)
        return element.text
