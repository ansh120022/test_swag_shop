class TestLogin:
    def test_auth(self, app):
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
        app.login.do_login()

        assert app.login.error_icon() == []
