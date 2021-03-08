"""Элемент - иконка корзины и счётчик на ней"""
from selenium.webdriver.common.by import By


class CartIcon:
    CART_COUNTER = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
