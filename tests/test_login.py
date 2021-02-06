import pytest
import allure
from locators.locators import LogInLocators
from pages.login_page import LogInPage
from config.config import Config

@pytest.mark.usefixtures("setup")
class TestLogIn:

    @allure.title("Login with valid data test")
    @allure.description("Test of login with valid data TC1)")
    def test_login_passed(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open_page()
        log_in_page.open_sign_in_page()
        log_in_page.click_sign_in()
        log_in_page.enter_user_credentials(Config.VALID_EMAIL, Config.VALID_PASSWORD)
        welcome_msg = "Hi {}".format(Config.VALID_NAME)

        assert welcome_msg in self.driver.find_element(*LogInLocators.welcome_message).text

        log_in_page.logout()

    @allure.title("Login with invalid password test")
    @allure.description("Test of login with valid email and invalid password (TC2a)")
    def test_login_failed(self):
        log_in_page = LogInPage(self.driver)
        log_in_page.open_page()
        log_in_page.open_sign_in_page()
        log_in_page.click_sign_in()
        log_in_page.enter_user_credentials(Config.VALID_EMAIL, Config.INVALID_PASSWORD)
        expected_error_message = "Access denied - wrong email address or password."
        access_denied_message = self.driver.find_element(*LogInLocators.access_denied_message)

        assert access_denied_message.is_displayed()
