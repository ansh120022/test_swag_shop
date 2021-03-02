"""Тесты для страницы продукта"""
import allure
from common.constants import AssertText as a, Subheaders as s


class TestProductPage:
    # @allure.epic("Страница товара")
    # @allure.story("Переход из каталога на страницу товара")
    # @allure.severity("Blocker")
    def test_go_to_product_details(self, app):
        """
        Проверка, что произведён переход именно на выбранный элемент
        """
        app.open_main_page()
        app.login.do_login_standart()

        product_name_text = app.product_list.item_name().text
        app.product_list.item_name().click()

        assert product_name_text == app.product.get_product_name()

    # @allure.epic("Страница товара")
    # @allure.story("Переход обратно в каталог")
    def test_back_button(self, app):
        app.open_main_page()
        app.login.do_login_standart()

        app.product_list.item_name().click()
        app.product.click_back()
        product_names = app.product_list.get_list_of_product_names()

        assert app.product_list.header() == s.products
        assert len(product_names) > 0, a.no_items

    # @allure.severity("Blocker")
    # @allure.epic("Страница товара")
    # @allure.story("Работа с корзиной")
    def test_cart(self, app):
        """
        Добавление и удаление из корзины на этой странице
        """
        app.open_main_page()
        app.login.do_login_standart()

        with allure.step("Добавить в корзину"):
            app.product_list.item_name().click()
            app.product.click_add_to_cart()

        assert app.product.cart_counter() == 1

        with allure.step("Удалить из корзины"):
            app.product.click_add_to_cart()
            assert app.product.cart_counter() == 0
