import pytest

from pytest_bdd import scenario, when, then, given, parser, parsers

from src.main.pages.home_screen import homeScreen
from src.main.pages.login_screen import loginScreen
from src.main.pages.toolbar_actions import toolBar
from src.main.pages.welcome_screen import welcomeScreen


# @pytest.mark.run(order=1)
@scenario('user_login.feature', 'Successful login')
def test_successful_login():
    pass


@given('Driver is up and launch the application')
def check_driver(appium_driver):
    global driver
    driver = appium_driver
    assert driver is not None, "Test Failed ! Driver is not initialized."


@when('User taps Log In button')
def tap_login_on_welcome_screen():
    global login
    login = welcomeScreen(driver).tap_login_btn()


@then(parsers.parse('Enter the email "{email}" in email field'))
def enter_email(email):
    login.type_email(email)


@then('Tap Next button')
def tap_next_button():
    login.tap_NEXT_btn()


@then(parsers.parse('Enter the psw "{psw}" in password field'))
def enter_password(psw):
    login.type_psw(psw)


@then('Tap Login button')
def tap_Login_button():
    login.tap_LOGIN_btn()


@then('Verify user is login successfully')
def verify_login():
    assert toolBar(driver).verify_the_profile_icon(), "Test Failed! User is not able to login successfully"
