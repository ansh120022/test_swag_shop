"""Тесты на авторизацию для аккаунтов в различных состояниях"""
from common.constants import AuthErrors, PAGES_URLS as urls, AssertText as a


class TestLogin:
    def test_standart_auth(self, app):
        """
        Позитивный тест
        1. Открыть сайт
        3. Ввести e-mail
        4. Ввести пароль
        5. Нажать кнопку LOGIN
        6. Нажать кнопку Register
        Ожидаемый результат:
        1. Сообщение об ошибке отсутствует
        2. Произведён переход на страницу Products
        """

        app.open_main_page()
        app.login.do_login_standart()
        product_names = app.product_list.get_list_of_product_names()

        assert app.login.error_icon() == []
        assert len(product_names) > 0, "Товары не отображаются"

    def test_do_login_performance(self, app):
        """
        Пользователь с медленным интернетом
        Авторируется, видит каталог
        """

        app.open_main_page()
        app.login.do_login_performance()
        product_names = app.product_list.get_list_of_product_names()

        assert app.login.error_icon() == []
        assert len(product_names) > 0, "Товары не отображаются"

    def test_do_login_locked(self, app):
        """
        Заблокированный пользователь получает ошибку, что он заблокированный
        """

        app.open_main_page()
        app.login.do_login_locked()

        assert app.login.error_icon() != [], a.no_error_icon
        assert app.login.get_error_text() == AuthErrors.locked_user, a.no_expected_error

    def test_do_login_nonexistent(self, app):
        """
        Авторизация несуществующего пользователя
        """

        app.open_main_page()
        app.login.do_login_nonexistent()

        assert (
            app.login.get_error_text() == AuthErrors.nonexistent_user
        ), a.no_expected_error
        assert app.login.error_icon() != [], a.no_error_icon

    def test_do_login_wrong_pass(self, app):
        """
        Авторизация с неправильным паролем
        """

        app.open_main_page()
        app.login.do_login_wrong_pass()

        assert (
            app.login.get_error_text() == AuthErrors.nonexistent_user
        ), a.no_expected_error
        assert app.login.error_icon() != [], a.no_error_icon

    def test_unauthorized_access(self, app):
        """Неавторизованному пользователю недоступны страницы сайта"""
        for url in urls:
            app.open_page(url)
            error = app.login.get_error_text()
            assert error == AuthErrors.unauthorized_error(url)
