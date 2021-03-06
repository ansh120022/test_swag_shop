from locators.left_menu import LeftMenu as p


class LeftMenuPage:
    def __init__(self, app):
        self.app = app

    def menu_button_element(self):
        return self.app.driver.find_element(*p.MENU_BUTTON)

    def close_button_element(self):
        return self.app.driver.find_element(*p.CLOSE_BUTTON)

    def all_items_element(self):
        return self.app.driver.find_element(*p.ALL_ITEMS)

    def about_button(self):
        return self.app.driver.find_element(*p.ABOUT)

    def logout_button(self):
        return self.app.driver.find_elements(*p.LOGOUT)

    def reset_app_button(self):
        return self.app.driver.find_element(*p.RESET_APP)

    def click_menu_button(self):
        self.menu_button_element.click()

    def click_close_button(self):
        self.close_button_element.click()

    def click_all_items(self):
        self.all_items_element.click()

    def click_about(self):
        self.about_element.click()

    def click_logout(self):
        self.logout_button.click()

    def click_reset_app(self):
        self.reset_app_element.click()
