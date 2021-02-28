"""Тесты для страниц Сheckout:Your Information и Сheckout:Overview"""
from common.constants import ClientData as client, Subheaders as s
import allure


class TestCheckout_YourInformationPage:
    @allure.epic("Оформление заказа")
    @allure.feature("Шаг заполнения данных клиента")
    @allure.story("Переход далее")
    @allure.severity("Blocker")
    def test_information_input(self, app):
        """Test the name and postal code input boxes on the checkout page."""

        with allure.step("Переход на страницу заказа"):
            app.open_main_page()
            app.login.do_login_standart()
            app.product_list.click_cart()
            app.cart.click_checkout()

        with allure.step("Попытка продолжить без заполнения формы"):
            app.checkout.click_continue()
            assert app.checkout.is_error_message_present()

        with allure.step("Заполнение формы с данными клиента"):
            app.checkout.input_first_name(client.firstname)
            app.checkout.input_last_name(client.surname)
            app.checkout.input_postal_code(client.postal_code)

        with allure.step("Проверка, что форма заполнена"):
            assert app.checkout.get_first_name() == client.firstname
            assert app.checkout.get_last_name() == client.surname
            assert app.checkout.get_postal_code() == client.postal_code

        with allure.step("Переход далее"):
            app.checkout.click_continue()
            assert app.checkout.get_subheader() == s.checkout_overview

    @allure.epic("Оформление заказа")
    @allure.feature("Заполнение данных клиента")
    @allure.story("Отмена, возврат обратно")
    def test_cancel(self, app):
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.click_cart()
        app.cart.click_checkout()
        app.checkout.click_cancel()
        assert app.cart.subheader() == s.your_cart


class TestCheckout_OverviewPage:
    @allure.epic("Оформление заказа")
    @allure.feature("Просмотр сформированного заказа")
    @allure.story("Отмена, возврат обратно")
    def test_cancel(self, app):
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.click_cart()
        app.cart.click_checkout()
        app.checkout.input_first_name(client.firstname)
        app.checkout.input_last_name(client.surname)
        app.checkout.input_postal_code(client.postal_code)

        app.checkout.click_continue()
        # overview_page.click_cancel()
        app.checkout.click_cancel()
        assert app.product_list.header() == s.products

    @allure.severity("Blocker")
    @allure.epic("Оформление заказа")
    @allure.feature("Просмотр сформированного заказа")
    @allure.story("Подтверждение заказа")
    def test_finish_button(self, app):
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.click_cart()
        app.cart.click_checkout()
        app.checkout.input_first_name(client.firstname)
        app.checkout.input_last_name(client.surname)
        app.checkout.input_postal_code(client.postal_code)
        app.checkout.click_continue()
        app.overview.click_finish()
        assert app.order_confirmation.subheader() == s.finish
