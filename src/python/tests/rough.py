import time

from appium import webdriver

browser_ios_caps = {
    "platformName": "iOS",
    "platformVersion": "15.0",  # iOS version
    "deviceName": "iPhone 13",
    "automationName": "XCUITest",
    "app": "bs://af51ca453133b05e06773e142ebff79aa4d286d2",  # Replace with your app's BrowserStack app-id
    "autoGrantPermissions": True,

}
user_name = "sumitbassan_85iO3o"
access_key = "EegGc23vRPmRj2GNxCCx"
BROWSER_URL = f"https://{user_name}:{access_key}@hub-cloud.browserstack.com/wd/hub"

driver = webdriver.Remote(BROWSER_URL, browser_ios_caps)

time.sleep(5)

print("Hello")

driver.quit()
