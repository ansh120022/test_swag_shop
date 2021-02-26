"""Элементы для страниц  Checkout:Your information и Checkout:Overview"""
from selenium.webdriver.common.by import By


class CheckoutPage:
    FIRSTNAME_TEXTBOX = (By.ID, "first-name")
    LASTNAME_TEXTBOX = (By.ID, "last-name")
    POSTALCODE_TEXTBOX = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.CLASS_NAME, "cart_cancel_link")
    CONTINUE_BUTTON = (By.CLASS_NAME, "btn_primary")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-button")
    SUBHEADER = (By.CLASS_NAME, "subheader")
