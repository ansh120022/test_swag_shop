"""Тесты на авторизацию для аккаунтов в различных состояниях"""
from common.constants import AuthErrors, PAGES_URLS as urls, AssertText as a
import pytest
from common.constants import Credentials as u
import allure
from pytest_testrail.plugin import pytestrail


class TestLogin:
    @allure.epic("Авторизация")
    @allure.story("Успешная авторизация")
    @allure.severity("Blocker")
    @pytestrail.case("C3")
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
        2. Произведён переход на страницу Products, отображаются товары
        """

        app.open_main_page()
        app.login.do_login(u.standard_user, u.passwd)
        product_names = app.product_list.get_list_of_product_names()

        assert app.login.error_icon() == []
        assert len(product_names) > 0, a.no_items

    @allure.epic("Авторизация")
    @allure.story("Неуспешная авторизация")
    @pytestrail.case("C4")
    @pytest.mark.parametrize(
        "login, passwd, expected_error",
        [
            (u.locked_out_user, u.passwd, AuthErrors.locked_user),
            (u.any_str, u.passwd, AuthErrors.nonexistent_user),
            (u.standard_user, u.any_str, AuthErrors.nonexistent_user),
        ],
    )
    def test_do_login_negative(self, app, login, passwd, expected_error):
        """
        Тесты для случаев, когда авторизация не должна пройти
        1. Заблокированный пользователь
        2. Несуществующий пользователь
        3. Стандартный пользователь с неверным паролем

        Во всех случаях результат: ошибка
        """

        app.open_main_page()
        app.login.do_login(login, passwd)

        assert app.login.error_icon() != [], a.no_error_icon
        assert app.login.get_error_text() == expected_error, a.no_expected_error

    @allure.epic("Авторизация")
    @allure.story("Доступ к сайту без авторизации")
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
