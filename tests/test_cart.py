"""Проверка всех функций корзины: возврат в каталог,
переход к оформлению, удаление товаров из корзины"""
import allure
from common.constants import AssertText as a, Subheaders as s


class TestCart:
    @allure.epic("Корзина")
    @allure.story("Возврат в каталог")
    def test_continue_shopping_button(self, app):
        """
        1.Переход из каталога в корзину
        2.Переход обратно
        3.Проверка, что снова отображается каталог
        """
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.click_cart()
        app.cart.click_continue_shopping()

        assert len(app.product_list.get_list_of_product_names()) > 0, a.no_items

    @allure.epic("Корзина")
    @allure.story("Переход к оформлению заказа")
    @allure.severity("Blocker")
    def test_checkout_button(self, app):
        """
        1. Перейти в корзину
        2. Нажать на кнопку Continue
        3. Открывается страница оформления заказа
        """
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.click_cart()
        app.cart.click_checkout()
        assert app.overview.get_subheader() == s.checkout_info, a.wrong_page

    @allure.epic("Корзина")
    @allure.story("Удаление из корзины")
    @allure.severity("Blocker")
    def test_remove_from_cart(self, app):
        """
        1. Добавляем все отображаемые товары в корзину
        2. Переходим в корзину
        3. Проверяем, что сумма не 0
        2. Удаляем все товары из корзины
        3. Отображается сумма 0
        """
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.add_all_to_cart()
        app.product_list.click_cart()
        assert app.cart.get_sum_prices() != 0.0
        app.cart.remove_all_from_cart()
        assert app.cart.get_sum_prices() == 0.0
