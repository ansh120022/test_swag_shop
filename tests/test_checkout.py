"""Тесты для страниц Сheckout:Your Information и Сheckout:Overview"""
from common.constants import ClientData as client


class TestCheckoutPage:
    """Testing the checkout page of saucedemo.com"""

    def test_information_input(self, app):
        """Test the name and postal code input boxes on the checkout page."""
        # Proceed to checkout page
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.click_cart()
        app.cart.click_checkout()

        # Try to continue without filling out information
        app.checkout.click_continue()
        assert app.checkout.is_error_message_present()

        # Input information
        app.checkout.input_first_name(client.firstname)
        app.checkout.input_last_name(client.surname)
        app.checkout.input_postal_code(client.postal_code)

        # Check data was successfully inserted and we can continue
        assert app.checkout.get_first_name() == client.firstname
        assert app.checkout.get_last_name() == client.surname
        assert app.checkout.get_postal_code() == client.postal_code
        app.checkout.click_continue()
        assert app.checkout.get_subheader() == "Checkout: Overview"

    def test_cancel_button(self, app):
        """Test the checkout page's cancel button."""
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.click_cart()
        app.cart.click_checkout()
        app.checkout.click_cancel()
        assert app.cart.subheader() == "Your Cart"
