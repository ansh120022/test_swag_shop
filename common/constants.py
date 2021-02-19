"""Файл с различными константами"""


class User:
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
