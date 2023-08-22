from src.main.pages.base_page import BasePage


class loginScreen(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.section = 'Login_Screen'

    def type_email(self, text):
        self.type(self.section, 'EMAIL_FIELD_XPATH', text)

    def tap_NEXT_btn(self):
        self.click(self.section, 'NEXT_BTN_XPATH')

    def tap_reset_password(self):
        self.click(self.section, 'RESET_PSW_LINK_ASCID')

    def tap_SIGNUP_btn(self):
        self.click(self.section, 'SIGNUP_BTN_ASCID')

    def type_psw(self, text):
        self.type(self.section, "PSW_FIELD_XPATH", text)

    def tap_LOGIN_btn(self):
        self.click(self.section, 'LOGIN_BTN_XPATH')

    def tap_backArrow_btn(self):
        self.click(self.section, 'BACK_BTN_ASCID')

    def verify_login(self):
        try:
            profile_icon = self.get_element('ToolBar', 'PROFILE_ICON_ID')
            is_logged_in = self.is_Element_Present(profile_icon)
            return is_logged_in
        except Exception:
            return False
