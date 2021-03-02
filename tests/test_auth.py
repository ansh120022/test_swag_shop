"""Тесты на авторизацию для аккаунтов в различных состояниях"""
from common.constants import AuthErrors, PAGES_URLS as urls, AssertText as a

# import allure
# from pytest_testrail.plugin import pytestrail


class TestLogin:
    # @allure.epic("Авторизация")
    # @allure.story("Обычный пользователь")
    # @allure.severity("Blocker")
    # @pytestrail.case("C3")
    def test_auth(self, app):
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

        assert app.login.error_icon() != []
        assert len(product_names) > 0, a.no_items

    # @allure.epic("Авторизация")
    # @allure.story("Заблокированный пользователь")
    # @pytestrail.case("C4")
    def test_do_login_locked(self, app):
        """
        1. Вводим заблокированный логин
        2. Получаем ошибку
        """

        app.open_main_page()
        app.login.do_login_locked()

        assert app.login.error_icon() != [], a.no_error_icon
        assert app.login.get_error_text() == AuthErrors.locked_user, a.no_expected_error

    # @allure.epic("Авторизация")
    # @allure.story("Несуществующий пользователь")
    def test_do_login_nonexistent(self, app):
        """
        1. Вводим несуществующий логин
        2. Получаем ошибку
        """

        app.open_main_page()
        app.login.do_login_nonexistent()

        assert (
            app.login.get_error_text() == AuthErrors.nonexistent_user
        ), a.no_expected_error
        assert app.login.error_icon() != [], a.no_error_icon

    # @allure.epic("Авторизация")
    # @allure.story("Неверный пароль")
    def test_do_login_wrong_pass(self, app):
        """
        1. Пользователь вводит неверный пароль
        2. Получает ошибку
        """

        app.open_main_page()
        app.login.do_login_wrong_pass()

        assert (
            app.login.get_error_text() == AuthErrors.nonexistent_user
        ), a.no_expected_error
        assert app.login.error_icon() != [], a.no_error_icon

    # @allure.epic("Авторизация")
    # @allure.story("Доступ к сайту без авторизации")
    def test_unauthorized_access(self, app):
        """
        1. Пользователь не авторизован
        2. Совершает переходы по прямым ссылкам
        3. Получает ошибку
        """

        for url in urls:
            app.open_page(url)
            error = app.login.get_error_text()
            assert error == AuthErrors.unauthorized_error(url)
