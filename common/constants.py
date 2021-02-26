"""Файл с различными константами"""


class Credentials:
    """Логины и пароли пользователей"""

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


class ButtonCaptions:
    """Названия разных кнопок"""

    remove = "REMOVE"
    add_to_cart = "ADD TO CART"


class AssertText:
    """Пояснения для assert'ов"""

    wrong_cart_counter = (
        "Число товаров на счётчике корзины не соответствует числу добавленных в корзину"
    )


class ClientData:
    """Данные клиента"""

    firstname = "Anastasia"
    surname = "Sh"
    postal_code = "603000"
