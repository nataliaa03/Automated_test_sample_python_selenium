import allure
import pytest
import selenium

from config.config import Config
from pages.login_page import LogInPage


@pytest.mark.usefixtures("setup")
class TestLogIn:
    error_message_too_many_attempts = "Too many account creations; please wait a while."
    error_message_access_denied = "Access denied - wrong email address or password."

    @allure.title("Login with valid data test")
    @allure.description("Test of login with valid data TC1)")
    def test_login_passed(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.sign_in()
        log_in_page.enter_user_credentials(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        login_msg = "You are now logged in."

        try:
            assert login_msg in log_in_page.get_flash_msg().text
            log_in_page.sign_out()
        except selenium.common.exceptions.TimeoutException:
            assert self.error_message_too_many_attempts in log_in_page.get_flash_msg_sign_in().text

    @allure.title("Login with invalid password test")
    @allure.description("Test of login with valid email and invalid password (TC2a)")
    def test_login_failed(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.sign_in()
        log_in_page.enter_user_credentials(Config.VALID_EMAIL, Config.INVALID_PASSWORD)

        assert log_in_page.get_flash_msg_sign_in().text in (
            self.error_message_access_denied, self.error_message_too_many_attempts)
