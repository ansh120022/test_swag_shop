class TestItemsList:
    def test_view(self, app):
        """Проверка факта отображения товаров в каталоге"""
        app.open_main_page()
        app.login.do_login_standart()
        product_names = app.product_list.get_list_of_product_names()
        assert len(product_names) > 0, "Товары не отображаются"

    def test_sort_z_to_a(self, app):
        """Проверка сортировки"""
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.do_sort_name_z_a()
        product_names = app.product_list.get_list_of_product_names()
        for i in range(len(product_names) - 1):
            assert product_names[i] >= product_names[i + 1], (
                f"Сортировка a-z не сработала: "
                f"{product_names[i]}, {product_names[i + 1]}"
            )
