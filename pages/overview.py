from locators.overview import OverviewPage as p
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger("app")


class OverviewPage:
    def __init__(self, app):
        self.app = app

    def get_subheader(self):
        element = self.app.driver.find_element(*p.SUBHEADER).text
        logger.info(f"Открылась страница {element}")
        return element

    def click_cancel(self):
        self.app.driver.find_element(*p.CANCEL_BUTTON).click()
        WebDriverWait(self.app.driver, 5).until(EC.url_changes)
        logger.info("Оформление заказа отменено")

    def click_finish(self):
        self.app.driver.find_element(*p.FINISH_BUTTON).click()
        WebDriverWait(self.app.driver, 5).until(EC.url_changes)
        logger.info("Оформление заказа успешно завершено")

    def get_subtotal(self):
        price_text = self.app.driver.find_element(*p.SUBTOTAL).text
        # Для получения только числового значения обрезаем часть строки "Item total: $"
        return float(price_text[13:])
