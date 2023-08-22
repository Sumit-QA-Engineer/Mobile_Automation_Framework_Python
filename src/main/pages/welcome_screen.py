from src.main.pages.base_page import BasePage
from src.main.pages.login_screen import loginScreen
# from src.main.pages.signUp_screen import signUpScreen


class welcomeScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.section = 'Welcome_Screen'

    def tap_login_btn(self):
        self.click(self.section,'LOGIN_BTN_ID')
        return loginScreen(self.driver)

    def tap_create_Acc_btn(self):
        self.click(self.section, 'CREATE_ACC_BTN_ID')

