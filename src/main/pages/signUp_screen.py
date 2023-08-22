#
# from src.main.pages.base_page import BasePage
#
#
# class signUpScreen(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.locators =()
#
#     def type_user_name(self, text):
#         self.type(self.locators.NAME_INP_FIELD, text)
#
#     def type_user_email(self, text):
#         self.type(self.locators.EMAIL_INP_FIELD, text)
#
#     def type_psw(self, text):
#         self.type(self.locators.PSW_INP_FIELD, text)
#
#     def tap_getStarted_btn(self):
#         self.click(self.locators.GET_STARTED_BTN)
#
#     def verify_captcha(self):
#         self.click(self.locators.CAPTCHA_CHECKBOX)