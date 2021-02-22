from common.constants import AuthErrors


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
        1. Сообщение об ошибке отсуствует
        2. Произведён переход на страницу Products
        """

        app.open_main_page()
        app.login.do_login_standart()

        assert app.login.error_icon() == []

    def test_do_login_locked(self, app):
        """
        Заблокированный пользователь получает ошибку
        о том, что он заблокированный
        """

        app.open_main_page()
        app.login.do_login_locked()

        assert app.login.error_icon() != []
        assert app.login.get_error_text() == AuthErrors.locked_user

    def test_do_login_performance(self, app):
        """
        Авторизация пользователя performance
        Всё ок
        """

        app.open_main_page()
        app.login.do_login_performance()

        assert app.login.error_icon() == []

    def test_do_login_nonexistent(self, app):
        """
        Авторизация несуществующего пользователя
        """

        app.open_main_page()
        app.login.do_login_nonexistent()

        assert app.login.get_error_text() == AuthErrors.nonexistent_user
        assert app.login.error_icon() != []

    def test_do_login_wrong_pass(self, app):
        """
        Авторизация с неправильным паролем
        """

        app.open_main_page()
        app.login.do_login_wrong_pass()

        assert app.login.get_error_text() == AuthErrors.nonexistent_user
        assert app.login.error_icon() != []
