"""Тесты для страницы каталога"""
from common.constants import ButtonCaptions as button, AssertText as a
import allure


class TestItemsList:
    @allure.epic("Страница каталога")
    @allure.story("Наличие товаров на странице")
    def test_view(self, app):
        """
        Проверка факта отображения товаров в каталоге
        """
        app.open_main_page()
        app.login.do_login_standart()
        product_names = app.product_list.get_list_of_product_names()
        assert len(product_names) > 0, a.no_items


class TestSorting:
    """
    Проверка сортировки в каталоге по алфавиту и цене
    """

    @allure.epic("Страница каталога")
    @allure.feature("Сортировка")
    @allure.story("Сортировка Z-A")
    def test_sort_z_to_a(self, app):
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.do_sort_name_z_a()
        product_names = app.product_list.get_list_of_product_names()
        for i in range(len(product_names) - 1):
            assert product_names[i] >= product_names[i + 1], (
                f"Сортировка z-a не сработала: "
                f"{product_names[i]}, {product_names[i + 1]}"
            )

    @allure.epic("Страница каталога")
    @allure.feature("Сортировка")
    @allure.story("Сортировка A-Z")
    def test_sort_a_to_z(self, app):
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.do_sort_name_a_z()
        product_names = app.product_list.get_list_of_product_names()
        for i in range(len(product_names) - 1):
            assert product_names[i] <= product_names[i + 1], (
                f"Сортировка a-z не сработала: "
                f"{product_names[i]}, {product_names[i + 1]}"
            )

    @allure.epic("Страница каталога")
    @allure.feature("Сортировка")
    @allure.story("Сортировка по возрастанию цены")
    def test_sort_low_to_high(self, app):
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.do_sort_price_low_high()
        product_prices = app.product_list.get_list_of_product_prices()
        for i in range(len(product_prices) - 1):
            assert product_prices[i] <= product_prices[i + 1], (
                f"Сортировка по возрастанию цены не сработала: {product_prices[i]},"
                f" {product_prices[i + 1]}"
            )

    @allure.epic("Страница каталога")
    @allure.feature("Сортировка")
    @allure.story("Сортировка по убыванию цены")
    def test_sort_high_to_low(self, app):
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.do_sort_price_high_low()
        product_prices = app.product_list.get_list_of_product_prices()
        for i in range(len(product_prices) - 1):
            assert product_prices[i] >= product_prices[i + 1], (
                f"Сортировка по убыванию цены не сработала: {product_prices[i]},"
                f" {product_prices[i + 1]}"
            )


class TestAddToCart:
    """
    Проверка взаимодействия с корзиной со страницы каталога
    """

    @allure.severity("Blocker")
    @allure.epic("Страница каталога")
    @allure.story("Добавление в корзину из каталога")
    def test_add_to_cart(self, app):
        with allure.step("Добавить товары, проверить счётчик корзины"):
            app.open_main_page()
            app.login.do_login_standart()
            product_elements = app.product_list.get_all_products()
            num_items_in_cart = 0
            assert (
                num_items_in_cart == app.product_list.get_cart_counter()
            ), a.wrong_cart_counter

        with allure.step("Добавить товары, проверить счётчик корзины"):
            for product in product_elements:
                add_cart_button = app.product_list.add_to_cart_button()
                add_cart_button.click()
                num_items_in_cart += 1
            assert (
                app.product_list.get_cart_counter() == num_items_in_cart
            ), a.wrong_cart_counter
            assert add_cart_button.text == button.remove

        with allure.step("Удалить товары, проверить счётчик корзины"):
            for _ in product_elements:
                remove_cart_button = app.product_list.remove_button()
                remove_cart_button.click()
                num_items_in_cart -= 1
            assert (
                app.product_list.get_cart_counter() == num_items_in_cart
            ), a.wrong_cart_counter
            assert remove_cart_button.text == button.add_to_cart
