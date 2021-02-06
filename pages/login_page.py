import logging
import allure
from locators.locators import LogInLocators
from helpers.webdriver_methods import move_to_and_click, send_keys
from selenium.webdriver.common.keys import Keys
from config.config import Config

class LogInPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    @allure.step("Opening timeanddate.com")
    def open_page(self):
        self.logger.info("Opening {} website".format(Config.APP_URL))
        self.driver.get(Config.APP_URL) #"https://www.timeanddate.com"

    @allure.step("Opening 'Sign in to timeanddate.com'")
    def open_sign_in_page(self):
        self.logger.info("Opening 'Sign in to timeanddate.com'")
        self.driver.find_element(*LogInLocators.user_menu).click()

    @allure.step("Opening 'sign in' page")
    def click_sign_in(self):
        self.logger.info("Opening sign in page")
        sign_in_button = self.driver.find_element(*LogInLocators.sign_in_button)
        move_to_and_click(self.driver, sign_in_button)


    @allure.step("Login with email and password.")
    def enter_user_credentials(self, email, password):
        self.logger.info("Entering email: {}".format(email) + " and password")
        email_text_box = self.driver.find_element(*LogInLocators.sign_in_email_input)
        send_keys(self.driver, email_text_box, email)
        passwd_text_box = self.driver.find_element(*LogInLocators.sign_in_password_input)
        send_keys(self.driver, passwd_text_box, password, Keys.ENTER)

    @allure.step("Sign out")
    def logout(self):
        self.logger.info("Signing out")
        self.driver.find_element(*LogInLocators.sign_out_link).click()
