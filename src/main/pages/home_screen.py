import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from src.main.pages.base_page import BasePage


class homeScreen(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.section = 'Home_Screen'

    # Add button and options functions
    def tap_add_btn(self):
        self.click(self.section, 'ADD_BTN_ASCID')

    def tap_new_folder(self):
        self.click(self.section, 'NEW_FOLDER_ASCID')

    def tap_upload_content(self):
        self.click(self.section, 'UPLOAD_CONTENT_ASCID')

    # Create Folder pop up actions
    def enter_folder_name(self, folder_name):
        self.type(self.section, 'FOLDER_NAME_FIELD_CLASS', folder_name)

    def tap_folder_create_btn(self):
        self.click(self.section, 'FOLDER_CREATE_BTN_XPATH')

    def tap_folder_cancel_btn(self):
        self.click(self.section, 'FOLDER_CANCEL_BTN_XPATH')

    def tap_folder_invite_checkbox(self):
        self.click(self.section, 'FOLDER_INVITE_CHECKBOX_CLASS')

    # Upload pop up actions
    def tap_select_file_to_upload(self):
        self.click(self.section, 'UPLOAD_FILE_XPATH')

    def tap_select_folder_to_upload(self):
        self.click(self.section, "UPLOAD_FOLDER_XPATH")

    # Item Pop up Menu action
    def tap_three_dot_for(self, text):
        Accessibility_ID = f"More actions for {text}"
        item = (AppiumBy.ACCESSIBILITY_ID, Accessibility_ID)
        element = self.wait_for_element_to_be_clickable(item)
        element.click()

    def tap_delete_item(self):
        self.click(self.section, 'ITEM_DELETE_XPATH')

    def tap_confirm_delete_item(self):
        self.click(self.section, 'ITEM_DELETE_CONFIRM_ID')

    # Verification Methods

    #
    # def verify_the_item_deleted(self, item_name, expected_result):
    #     time.sleep(3)
    #     item = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{item_name}']")
    #     is_item_deleted = not self.is_Element_Present(item)
    #     print(is_item_deleted)
    #
    #     if is_item_deleted:
    #         actual_result = f"Actual Result - {expected_result.replace('should be', 'is').replace('should', 'is')}"
    #     else:
    #         actual_result = f"Actual Result - {expected_result.replace('should be', 'is not').replace('should', 'is not')}"
    #
    #     assert is_item_deleted, f"Test failed! {actual_result}"
    #
    #     return actual_result
    #


