from selenium.webdriver.common.by import By


class OverviewPage:
    CANCEL_BUTTON = (By.CLASS_NAME, "cart_cancel_link")
    FINISH_BUTTON = (By.CLASS_NAME, "btn_action")
    SUBHEADER = (By.CLASS_NAME, "subheader")
    SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
