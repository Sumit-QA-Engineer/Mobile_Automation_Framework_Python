import pytest
from pytest_bdd import scenario, when, then, given, parsers

from src.main.pages.home_screen import homeScreen
from src.main.pages.login_screen import loginScreen

# @pytest.mark.run(order=4)
@scenario('delete_content.feature', 'Delete Folder')
def test_delete_folder():
    pass

# @pytest.mark.run(order=5)
@scenario('delete_content.feature', 'Delete File')
def test_delete_file():
    pass


@given('User is logged in the application')
def pre_condition_1(appium_driver):
    global driver
    driver = appium_driver
    assert loginScreen(driver).verify_login(), ("!!!! Test Failed! Pre-condition does not met - User is not "
                                                "logged in the application !!!!")


@given(parsers.parse('"{item_name}" file is present on home screen'))
@given(parsers.parse('"{item_name}" folder is present on home screen'))
def pre_condition_2(item_name):
    global home
    home = homeScreen(driver)
    assert home.verify_the_item_by_text(item_name), (f"!!! Test Failed! 2nd Pre-Condition does not met - {item_name} is "
                                             f"not present on home screen")


@when(parsers.parse('User taps on three dot menu button of "{item_name}" file'))
@when(parsers.parse('User taps on three dot menu button of "{item_name}" folder'))
def tap_3_dot_button(item_name):
    home.tap_three_dot_for(item_name)


@then('Tap Delete option from the pop up menu')
def tap_new_folder_option():
    home.tap_delete_item()


@then('Tap Delete button on the Delete confirmation pop up')
def confirm_delete_popUp():
    home.tap_confirm_delete_item()


@then(parsers.parse('Verify "{item_name}" file is deleted'))
@then(parsers.parse('Verify "{item_name}" folder is deleted'))
def verify_item_is_deleted(item_name):
    is_deleted = home.verify_the_item_by_text(item_name)
    assert is_deleted is not True, f"!!!Test Failed!!! - User is not able to delete {item_name} folder {is_deleted}"
