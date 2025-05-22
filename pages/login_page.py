import logging

import allure
import selenium
from selenium.webdriver import ActionChains

from locators.locators import LogInLocators
from helpers.webdriver_methods import move_to_and_click, send_keys, wait_until_el_visible
from selenium.webdriver.common.keys import Keys
from config.config import Config


class LogInPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Navigate to home page")
    def navigate_to_home_page(self):
        self.logger.info("Opening {} website".format(Config.APP_URL))
        self.driver.get(Config.APP_URL)

    @allure.step("Click on Agree of privacy consent")
    def click_agree_or_skip(self):
        try:
            self.driver.find_element(*LogInLocators.agree_button).click()
            self.logger.info("Clicked 'Agree' button")
        except (
                selenium.common.exceptions.ElementNotInteractableException,
                selenium.common.exceptions.NoSuchElementException):
            self.logger.info("Agree of privacy consent - no need to click.")

    @allure.step("Select 'Sign in' option")
    def select_sign_in(self):
        self.logger.info("Signing in")
        self.select_account_option(*LogInLocators.sign_in_button)

    @allure.step("Select 'Sign out' option")
    def sign_out(self):
        self.logger.info("Signing out")
        self.select_account_option(*LogInLocators.sign_out_button)

    @allure.step("Login with email and password.")
    def enter_user_credentials(self, email, password):
        self.logger.info(f"Entering email: {email} and password")
        email_text_box = self.driver.find_element(*LogInLocators.sign_in_email_input)
        send_keys(email_text_box, email)
        passwd_text_box = self.driver.find_element(*LogInLocators.sign_in_password_input)
        send_keys(passwd_text_box, password, Keys.ENTER)

    @allure.step("Get flash message")
    def get_flash_msg(self):
        wait_until_el_visible(self.driver, *LogInLocators.flash_message)
        return self.driver.find_element(*LogInLocators.flash_message)

    @allure.step("Get flash message in Sign in window")
    def get_flash_msg_sign_in(self):
        wait_until_el_visible(self.driver, *LogInLocators.login_error_message)
        return self.driver.find_element(*LogInLocators.login_error_message)

    def sign_in(self):
        self.navigate_to_home_page()
        self.click_agree_or_skip()
        self.select_sign_in()

    def select_account_option(self, by, option_button):  # eg: *LogInLocators.sign_out_button
        my_account_icon = self.driver.find_element(*LogInLocators.my_account_icon)
        ActionChains(self.driver).move_to_element(my_account_icon).perform()
        button = self.driver.find_element(by, option_button)
        move_to_and_click(self.driver, button)
