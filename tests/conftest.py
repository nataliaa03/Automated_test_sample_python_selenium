import uuid

import allure
import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver import DesiredCapabilities

from config.config import Config


@pytest.fixture()
def setup(request):
    remote_url = "http://localhost:4444/wd/hub"

    options = get_default_chrome_options()
    capabilities = DesiredCapabilities.CHROME.copy()
    driver = webdriver.Remote(command_executor=remote_url, options=options, desired_capabilities=capabilities)
    driver.maximize_window()

    driver.implicitly_wait(Config.DEFAULT_TIMEOUT)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()


def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--incognito")
    options.add_argument("--disable-autofill-keyboard-accessory-view")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--no-first-run")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.add_argument("--user-data-dir=/tmp/selenium-profile-" + str(uuid.uuid4()))

    return options
