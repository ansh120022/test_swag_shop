"""Тесты для страницы каталога"""


class TestItemsList:
    def test_view(self, app):
        """Проверка факта отображения товаров в каталоге"""
        app.open_main_page()
        app.login.do_login_standart()
        product_names = app.product_list.get_list_of_product_names()
        assert len(product_names) > 0, "Товары не отображаются"


class TestSorting:
    """Проверка сортировки в каталоге по алфавиту и цене"""

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
