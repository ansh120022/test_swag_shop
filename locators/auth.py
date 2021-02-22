"""Элементы на странице входа"""
from selenium.webdriver.common.by import By


class Login:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_SUBMIT = (By.ID, "login-button")

    ERROR_ICON = (By.CLASS_NAME, "error-button")
    ERROR_TEXT = (By.TAG_NAME, "h3")
