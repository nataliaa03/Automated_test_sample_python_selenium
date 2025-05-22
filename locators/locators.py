from selenium.webdriver.common.by import By


class LogInLocators:
    agree_button = (By.XPATH, "//button/span[text()='AGREE']")
    my_account_icon = (By.CSS_SELECTOR, '.site-nav__menu--my-account a i')
    sign_in_button = (By.XPATH, "//a[contains(text(), 'Sign in')]")
    sign_out_button = (By.XPATH, "//a[contains(text(), 'Sign out')]")

    create_account_button = (By.XPATH, "//a[contains(text(), 'Register')]")

    sign_in_email_input = (By.XPATH, "//input[@id='email']")
    sign_in_password_input = (By.XPATH, "//input[@id='password']")
    access_denied_message = (By.XPATH, "//*[contains(text(), 'Access denied - wrong email address or password.')]")
    login_error_message = (By.CSS_SELECTOR, "#errormessage")

    flash_message = (By.CSS_SELECTOR, "#anw")


class RegisterLocators:
    register_name = (By.XPATH, "//input[@name='fullname']")
    register_email = (By.XPATH, "//input[@name='email']")
    register_password = (By.XPATH, "//input[@name='password']")
    register_password1 = (By.XPATH, "//input[@name='password1']")

    create_account_button = (By.ID, "create")
    register_error_msg = (By.ID, "errormessage")

# The password must be entered and then repeated exactly.
