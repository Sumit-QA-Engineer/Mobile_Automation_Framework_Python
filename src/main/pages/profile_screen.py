import time

from appium.webdriver.common.appiumby import AppiumBy

from src.main.pages.base_page import BasePage


class profileScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.section = 'Profile_Screen'

    def tap_logout(self):
        self.click(self.section, 'LOGOUT_OPTION_ID')

    def tap_confirm_logout(self):
        self.click(self.section, 'LOGOUT_CONFIRM_ID')

    def verify_user_logout(self, item_name):
        try:
            item = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{item_name}']")
            wait_element = self.wait_for_element_to_be_located(item)
            is_item_displayed = self.is_Element_Present(wait_element)
            return is_item_displayed
        except Exception:
            return False


