import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pages.auth import LoginPage
from pages.product_list import ProductList
from pages.product import ProductPage
from pages.cart import CartPage
from pages.checkout import CheckoutPage
from pages.overview import OverviewPage
from pages.order_confirmation import OrderConfirmationPage
from pages.left_menu import LeftMenuPage

logger = logging.getLogger("app")


class Application:
    def __init__(self, headless, url):
        options: Options = Options()
        if headless:
            options.add_argument("--headless")
        self.url = url
        try:
            self.driver = webdriver.Chrome(
                ChromeDriverManager().install(), options=options
            )
        except ValueError:
            self.driver = webdriver.Chrome(r"C:\chromedriver.exe", options=options)
        self.login = LoginPage(self)
        self.product_list = ProductList(self)
        self.product = ProductPage(self)
        self.cart = CartPage(self)
        self.checkout = CheckoutPage(self)
        self.overview = OverviewPage(self)
        self.order_confirmation = OrderConfirmationPage(self)
        self.left_menu = LeftMenuPage(self)

    def open_main_page(self):
        logger.info("Открылась главная страница")
        self.driver.get(self.url)

    def open_page(self, url: str):
        logger.info(f"Запрошена страница {self.url}{url}")
        self.driver.get(f"{self.url}{url}")

    def browser_close(self):
        logger.info("Закрытие браузера")
        self.driver.quit()
