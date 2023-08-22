import os
from datetime import datetime

import allure
from allure_commons.types import AttachmentType

from src.main.utilities.propertiesReader import get_main_project_directory


def capture_screenshot(driver, test_name):
    project_directory = get_main_project_directory("mobile_aautomation_pytest_bdd")
    screenshots_dir = os.path.join(project_directory, "screenshots\\" + test_name)

    # print(screenshots_dir)

    os.makedirs(screenshots_dir, exist_ok=True)

    # Generate a timestamp for the screenshot file name
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M")

    # Construct the screenshot file name with test name and timestamp
    screenshot_file = f"{test_name}_{timestamp}.png"

    # Take the screenshot and save it in the "screenshots" directory
    driver.save_screenshot(os.path.join(screenshots_dir, screenshot_file))
    allure.attach(driver.get_screenshot_as_png(), name=screenshot_file, attachment_type=AttachmentType.PNG)
    print("Screenshot is saved in -", screenshots_dir)
