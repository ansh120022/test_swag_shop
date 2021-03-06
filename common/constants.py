"""Файл с различными константами"""


class Credentials:
    """Логины и пароли тестовых пользователей"""

    standard_user = "standard_user"
    locked_out_user = "locked_out_user"
    problem_user = "problem_user"
    performance_user = "performance_glitch_user"
    passwd = "secret_sauce"
    any_str = "blablablah"


class AuthErrors:
    """Тексты ошибок авторизации"""

    epic_sadface = "Epic sadface"
    nonexistent_user = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    locked_user = "Epic sadface: Sorry, this user has been locked out."

    @staticmethod
    def unauthorized_error(url):
        return f"Epic sadface: You can only access '/{url}' when you are logged in."


class ButtonCaptions:
    """Названия разных кнопок"""

    remove = "REMOVE"
    add_to_cart = "ADD TO CART"


class AssertText:
    """Пояснения для assert'ов"""

    wrong_cart_counter = (
        "Число товаров на счётчике корзины не соответствует числу добавленных в корзину"
    )
    no_expected_error = "Ошибка не возникла, либо её текст не совпадает с ожидаемым"
    no_error_icon = "Ожидаемая иконка ошибки отсутствует"
    no_items = "Товары не отображаются"
    wrong_page = "Произведён переход на неверную страницу"


class ClientData:
    """Данные клиента"""

    firstname = "Анастасия"
    surname = "Шаховнина"
    postal_code = "603000"


class Subheaders:
    """Заголовки страниц"""

    products = "Products"
    finish = "Finish"
    checkout_info = "Checkout: Your Information"
    checkout_overview = "Checkout: Overview"
    your_cart = "Your Cart"


# Список страниц сайта
PAGES_URLS = ["inventory.html", "cart.html"]
