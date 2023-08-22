import pytest

from pytest_bdd import scenario, when, then, given, parser, parsers

from src.main.pages.home_screen import homeScreen
from src.main.pages.login_screen import loginScreen
from src.main.pages.profile_screen import profileScreen
from src.main.pages.toolbar_actions import toolBar


# @pytest.mark.run(order=6)
@scenario('user_logout.feature', 'Successful Logout')
def test_user_logout():
    pass


@given('User is logged in the application')
def pre_condition_1(appium_driver):
    global driver
    driver = appium_driver
    assert loginScreen(driver).verify_login(), ("!!!! Test Failed! Pre-condition does not met - User is not "
                                                       "logged in the application !!!!")


@when('User taps on Profile Icon at toolbar')
def open_profile_scree():
    global profile
    profile = toolBar(driver).tap_profile_icon()


@then('Tap on Logout option on the Profile screen')
def tap_logout_option():
    profile.tap_logout()


@then('Tap on Logout button on Logout confirmation pop up')
def confirm_logout():
    profile.tap_confirm_logout()


@then('Verify user logouts from the application')
def verify_logout():
    assert profile.verify_the_item_by_text("Sign In to Your Account"), "!!!!! TEST FAILED !!!!!, User is not able to logout"
