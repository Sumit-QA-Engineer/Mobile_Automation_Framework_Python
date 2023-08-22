import pytest
from pytest_bdd import scenario, when, then, given, parsers

from src.main.pages.home_screen import homeScreen
from src.main.pages.login_screen import loginScreen
from src.main.pages.profile_screen import profileScreen
from src.main.pages.toolbar_actions import toolBar

driver = None

# @pytest.mark.run(order=3)
@scenario('upload_content.feature', 'Upload File')
def test_upload_file():
    pass


def setup_method(appium_driver):
    print("hello world")


@given('Driver is Up')
def pre_condition_1(appium_driver):
    print("inside pre condition 1")
    global driver
    driver = appium_driver
    assert driver is not None, "!!!! Test Failed! First Pre-condition does not met - Driver is not Up !!!!"


@given('User is logged in the application')
def pre_condition_2():
    assert toolBar(driver).verify_the_profile_icon(), "!!! Test Failed !!! 2nd Pre-condition does nto met - User is not logged in !!!"


@when('User tap on Add button')
def tap_3_dot_button():
    global home
    home = homeScreen(driver)
    home.tap_add_btn()


@then('Tap on Upload Content option')
def tap_upload_content_option():
    home.tap_upload_content()


@then('Tap on "Select files to upload" option')
def tap_select_files_to_upload_option():
    home.tap_select_file_to_upload()


@then(parsers.parse('Select the "{item_name}" from the device manager'))
def select_file_from_device(item_name):
    home.select_image_from_device(item_name)


@then(parsers.parse('Verify "{item_name}" is uploaded in the application'))
def verify_file_is_uploaded(item_name):
    assert home.verify_the_item_by_text(item_name), f"{item_name} file is not uploaded in the application"
