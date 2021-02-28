from selenium.webdriver.common.by import By


class LeftMenu:
    SIDE_MENU = By.XPATH, "//div[@class='bm-menu']"
    SIDE_MENU_CLOSE_BUTTON = By.XPATH, "//div[@class='bm-cross-button']"
    ALL_ITEMS = (By.XPATH, "//a[@id='inventory_sidebar']")
    ABOUT = (By.XPATH, "//a[@id='about_sidebar']")
    LOGOUT = (By.XPATH, "//a[@id='logout_sidebar']")
    RESET_APP = (By.XPATH, "//a[@id='reset_sidebar']")
