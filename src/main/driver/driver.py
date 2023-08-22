import sys

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

sys.path.append(r"/")
from src.main.utilities.propertiesReader import readProperties


def get_BS_properties(os_name, user_name, access_key):
    global desired_caps
    cap_prop = readProperties("browserStack.properties")
    URL = f"https://{user_name}:{access_key}@hub-cloud.browserstack.com/wd/hub"
    os_name = os_name.lower()
    desired_caps = {
        "platformName": cap_prop.get_key(os_name, f'{os_name}_platform_name'),
        "automationName": cap_prop.get_key(os_name, f'{os_name}_automation_name'),
        "deviceName": cap_prop.get_key(os_name, f'{os_name}_device_name'),
        "platformVersion": cap_prop.get_key(os_name, f'{os_name}_platform_version'),
        "noReset": cap_prop.get_key(os_name, f'{os_name}_noReset'),
        "autoGrantPermissions": cap_prop.get_key(os_name, f'{os_name}_autoGrantPermissions'),
        "app": cap_prop.get_key(os_name, f'{os_name}_app'),
    }

    return desired_caps, URL


def get_local_properties(os_name, port):
    global desired_caps
    cap_prop = readProperties("local.properties")
    URL = f"http://localhost:{port}/wd/hub"
    os_name = os_name.lower()
    desired_caps = {
        "automationName": cap_prop.get_key(os_name, f'{os_name}_automation_name'),
        "platformName": cap_prop.get_key(os_name, f'{os_name}_platform_name'),
        "deviceName": cap_prop.get_key(os_name, f'{os_name}_device_name'),
        "platformVersion": cap_prop.get_key(os_name, f'{os_name}_platform_version'),
        "app": cap_prop.get_key(os_name, f'{os_name}_app'),
        "appPackage": cap_prop.get_key(os_name, f'{os_name}_appPackage'),
        "appActivity": cap_prop.get_key(os_name, f'{os_name}_appActivity'),
        "udid": cap_prop.get_key(os_name, f'{os_name}_udid'),
        "noReset": cap_prop.get_key(os_name, f'{os_name}_noReset'),
        "autoGrantPermissions": cap_prop.get_key(os_name, f'{os_name}_autoGrantPermissions'),
    }

    return desired_caps, URL


def get_realDevice_properties(os_name):
    pass


class AppiumDriver:

    def __init__(self):
        self.config = readProperties('config.properties')
        self.driver = None

    def driverSetup(self):
        global URL, desired_caps
        platform = self.config.get_key('Configuration', 'platform')
        os_name = self.config.get_key('Configuration', 'os_name')

        if platform.lower() == 'bs':
            user_name = self.config.get_key('Configuration', 'user_name')
            access_key = self.config.get_key('configuration','access_key')
            desired_caps, URL = get_BS_properties(os_name,user_name,access_key)
        elif platform.lower() == 'local':
            port = self.config.get_key('Configuration', 'port')
            desired_caps, URL = get_local_properties(os_name, port)
        else:
            raise Exception("Please define the valid platform and os in config.properties files")

        self.driver = webdriver.Remote(URL, desired_caps)
        self.driver.implicitly_wait(10)
        return self.driver

    def driverTeardown(self):
        self.driver.quit()
