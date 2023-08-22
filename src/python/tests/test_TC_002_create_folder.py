import pytest

from pytest_bdd import scenario, when, then, given, parser, parsers

from src.main.pages.home_screen import homeScreen
from src.main.pages.login_screen import loginScreen

# @pytest.mark.run(order=2)
@scenario('create_folder.feature', 'Create_folder')
def test_createFolder():
    pass


@given('User is logged in to the application')
def user_logged_in(appium_driver):
    global driver
    driver = appium_driver
    assert loginScreen(driver).verify_login(), \
        ("!!!! Test Failed! Pre-condition does not met - User is not logged in the "
         "application !!!!")


# When tests
@when('User taps on the Add button')
def tap_add_button():
    global home
    home = homeScreen(driver)
    home.tap_add_btn()


@then('User taps on the New Folder option')
def tap_new_folder_option():
    home.tap_new_folder()


@then(parsers.parse('User enters folder name "{folder_name}" in the input field'))
def enter_folder_name(folder_name):
    home.enter_folder_name(folder_name)


@when('User taps on the Create button')
def tap_create_button():
    home.tap_folder_create_btn()


@then(parsers.parse('Verify "{folder_name}" folder is created successfully'))
def verify_folder_created(folder_name):
    home.verify_the_item_by_text(folder_name)
