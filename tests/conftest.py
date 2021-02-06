import allure
import pytest
from allure_commons.types import AttachmentType
from utils.drivers import GetDriver
from config.config import Config

@pytest.fixture()
def setup(request):
    driver = GetDriver.get_driver(Config.DEFAULT_DRIVER) # chrome is default
    driver.implicitly_wait(Config.DEFAULT_TIMEOUT)
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    driver.quit()
