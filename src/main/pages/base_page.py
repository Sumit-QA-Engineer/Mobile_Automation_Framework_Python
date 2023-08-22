import logging
import subprocess
import time

import pytest
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from src.main.logging.bdd_logging import get_logger, setup_logging
from src.main.utilities.propertiesReader import readProperties


locator_prop = readProperties("locators.Properties")

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        setup_logging(log_file='test.log', log_level=logging.DEBUG)
        self.logger = get_logger('test_logger')


    # def wait_for_element_visible(self, element, timeout=10):
    #     try:
    #         WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(element))
    #     except TimeoutException:
    #         raise TimeoutException(f"Element {element} not visible after {timeout} seconds.")


    def run_adb_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                print(f"Error executing adb command: {result.stderr}")
                return None
        except Exception as e:
            print(f"Exception occurred: {e}")
            return None

    def click(self, section, key):
        element = self.get_element(section, key)
        self.logger.info(f"Clicking on element - {element}")
        wait_cl = self.wait_for_element_to_be_clickable(element)
        wait_cl.clear()
        wait_cl.click()


    def type(self, section, key, text):

        element = self.get_element(section, key)
        self.logger.info(f"Typing {text} in the element - {element}")
        # wait_el = self.wait_for_element_to_be_located(element, 20)
        # wait_el.clear()
        element.send_keys(text)


    def tap_keyboard_enter_btn(self):
        self.run_adb_command("adb shell input keyevent 66")

    def is_Element_Present(self, element):
        try:
            self.logger.info(f"Driver is finding the element - {element.text} on display")
            return element.is_displayed()
        except NoSuchElementException:
            self.logger.error(f"Driver is not able to find the element - {element.text}")
            return False

    def get_Element_Text(self, element):
        try:
            text = element.text
            # logging.info(f"Driver gets the {text} from this element - {element}")
            return text
        except Exception as e:
            print(f"Failed to get element text: {e}")
            return None

    def assert_text_equal(self, actual_text, expected_text):
        assert actual_text == expected_text, (f"Assertion Error: Actual text '{actual_text}' does not match expected "
                                              f"text '{expected_text}'")

    def wait_for_element_to_be_located(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise Exception(f"Element with locator '{locator}' not found after {timeout} seconds.")

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return element
        except TimeoutException:
            raise Exception(f"Element with locator '{locator}' not found after {timeout} seconds.")

    def safe_click(self, key, section):
        MAX_RETRIES = 3
        retries = 0

        while retries < MAX_RETRIES:
            try:
                self.get_element(key, section).click()
                return True
            except StaleElementReferenceException:
                retries += 1
                time.sleep(1)  # Wait for a moment before retrying to avoid overloading the application

        return False

    def get_element(self, section, key):
        global element
        by = key.split("_")[-1]
        value = locator_prop.get_key(section, key)
        try:
            if by == "ASCID":
                element = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=value)
            elif by == 'XPATH':
                element = self.driver.find_element(by=AppiumBy.XPATH, value=value)
            elif by == 'ID':
                element = self.driver.find_element(by=AppiumBy.ID, value=value)
            elif by == 'CLASS':
                element = self.driver.find_element(by=AppiumBy.CLASS_NAME, value=value)
            else:
                print(f"please add identifier with {key} locator in properties files")
        except Exception:
            return pytest.raises(NoSuchElementException)
            # assert False, f"!!!!There is no such {element} present on screen to perform click action!!!!!"

        return element

    def select_image_from_device(self, file_name):
        self.click('Android_Device_Manager', 'HAMBURGER_MENU_ASCID')
        self.safe_click('Android_Device_Manager', 'EMULATOR_STORAGE_XPATH')
        self.click('Android_Device_Manager', 'IMAGE_TAG_XPATH')

        image = self.driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[@text='{file_name}']")
        is_image_present = self.is_Element_Present(image)

        assert is_image_present, f"There is no {file_name} file is available in device"
        image.click()

    def verify_the_item_by_text(self, item_name):
        time.sleep(2)
        try:
            item = self.driver.find_element(by=AppiumBy.XPATH, value=f"//android.widget.TextView[@text='{item_name}']")
            return self.is_Element_Present(item)
        except Exception:
            return False
