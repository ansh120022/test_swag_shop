"""Проверка всех функций корзины: возврат в каталог,
переход к оформлению, удаление товаров из корзины"""


class TestCart:
    def test_continue_shopping_button(self, app):
        """1.Переход с главной страницы в корзину и обратно
        Проверка, что при обратном переходе снова отображается каталог"""
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.click_cart()
        app.cart.click_continue_shopping()

        assert len(app.product_list.get_list_of_product_names()) > 0

    def test_checkout_button(self, app):
        """Переход к оформлению заказа"""
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.click_cart()
        app.cart.click_checkout()

        # TODO assert

    def test_remove_from_cart(self, app):
        """Проверка удаления из корзины"""
        app.open_main_page()
        app.login.do_login_standart()
        app.product_list.add_all_to_cart()
        app.product_list.click_cart()
        app.cart.remove_all_from_cart()

    # TODO assert
