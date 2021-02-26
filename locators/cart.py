"""Элементы на странице корзины"""
from selenium.webdriver.common.by import By


class CartPage:
    CONTINUE_SHOPPING_BUTTON = (By.CLASS_NAME, "btn_secondary")
    CHECKOUT_BUTTON = (By.CLASS_NAME, "checkout_button")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")
    SUBHEADER = (By.CLASS_NAME, "subheader")
