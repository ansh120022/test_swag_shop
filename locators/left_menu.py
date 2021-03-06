"""Элементы меню, которое появляется в левой части магазина по клику на кнопку-бургер"""
from selenium.webdriver.common.by import By


class LeftMenu:
    MENU_BUTTON = (By.ID, "bm-burger-button")
    CLOSE_BUTTON = (By.ID, "react-burger-cross-btn")
    ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    ABOUT = (By.ID, "about_sidebar_link")
    LOGOUT = (By.ID, "logout_sidebar_link")
    RESET_APP = (By.ID, "reset_sidebar_link")
