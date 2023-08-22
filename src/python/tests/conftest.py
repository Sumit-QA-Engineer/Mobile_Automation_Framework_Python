import re
import sys
import pytest

sys.path.append(r"C:\Users\subassan\PycharmProjects\mobile_aautomation_pytest_bdd")

from src.main.utilities.capture_screenshot import capture_screenshot

from src.main.driver.driver import AppiumDriver


def pytest_bdd_apply_tag(tag, function):
    if tag.startswith('run(order='):
        order = int(tag.split('=')[1].rstrip(')'))
        marker = pytest.mark.run(order=order)
        marker(function)
        return True
    else:
        # Fall back to the default behavior of pytest-bdd
        return None


# Register the custom marker 'run' in pytest.ini (if not already done)
def pytest_collection_modifyitems(config, items):
    def get_order(item):
        marker = item.get_closest_marker("run")
        return marker.kwargs["order"] if marker else 0

    items.sort(key=get_order)


def pytest_configure(config):
    config.addinivalue_line("markers", "run(order): mark a test to run with order")
    config.addinivalue_line("markers", "smoke: mark a test as smoke")


@pytest.fixture(scope="session")
def appium_driver(request):
    dr = AppiumDriver()
    driver = dr.driverSetup()
    return driver


@pytest.fixture(scope="session", autouse=True)
def teardown(appium_driver):
    yield
    appium_driver.quit()


@pytest.fixture(scope="function", autouse=True)
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    if item.rep_call.failed:
        capture_screenshot(appium_driver, re.findall(r'^\w+', item.name)[0])


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# def pytest_addoption(parser):
#     parser.addoption("--platform", choices=["android", "ios"])
#     parser.addoption("--appium-port", type=int, default=4723, help="Port number for Appium server")
#
#
# @pytest.fixture(scope="session", autouse=True)
# def platform(request):
#     platform_value = request.config.getoption("--platform")
#     if platform_value:
#         os.environ["PLATFORM"] = platform_value
#     return os.environ.get("PLATFORM", "android")
#
#
# @pytest.fixture(scope="session", autouse=True)
# def appium_port(request):
#     return request.config.getoption("--appium-port")
