from src.main.pages.base_page import BasePage
from src.main.pages.profile_screen import profileScreen


class toolBar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.section = 'ToolBar'

    def tap_profile_icon(self):
        self.click(self.section, 'PROFILE_ICON_ID')
        return profileScreen(self.driver)

    def verify_the_profile_icon(self):
        try:
            profileIcon = self.get_element(self.section,'PROFILE_ICON_ID')
            return self.is_Element_Present(profileIcon)
        except Exception:
            print(Exception)
            return False

