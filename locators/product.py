"""Элементы на странице товара"""
from selenium.webdriver.common.by import By


class ProductPage:
    PRICE = (By.CLASS_NAME, "inventory_details_price")
    ADD_TO_CART = (By.CLASS_NAME, "btn_inventory")
    BACK_BUTTON = (By.CLASS_NAME, "inventory_details_back_button")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_details_name")
