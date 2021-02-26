class TestProductPage:
    def test_go_to_product_details(self, app):
        """Проверка, что произведён переход именно на выбранный эелемент"""
        app.open_main_page()
        app.login.do_login_standart()

        product_name_text = app.product_list.item_name().text
        app.product_list.item_name().click()

        assert product_name_text == app.product.get_product_name()

    def test_back_button(self, app):
        """Проверка, перехода назад"""
        app.open_main_page()
        app.login.do_login_standart()

        app.product_list.item_name().click()
        app.product.click_back()
        product_names = app.product_list.get_list_of_product_names()

        assert app.product_list.header() == "Products"
        assert len(product_names) > 0, "Товары не отображаются"

    def test_cart(self, app):
        """Добавление и удаление из корзины на этой странице"""
        app.open_main_page()
        app.login.do_login_standart()

        # Добавление в корзину
        app.product_list.item_name().click()
        app.product.click_add_to_cart()

        assert app.product.cart_counter() == 1

        # удаление из корзины
        app.product.click_add_to_cart()
        assert app.product.cart_counter() == 0
