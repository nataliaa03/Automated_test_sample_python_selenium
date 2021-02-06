from selenium.webdriver.common.by import By

class LogInLocators:
    user_menu = (By.XPATH, "//i[@class='i-font i-account_circle site-nav__desktop-title']")
    sign_in_button = (By.XPATH, "//section[@class='article__body article__body--right']//a[contains(text(), 'Sign In')]")

    create_account_button = (By.XPATH, "//section[@class='article__body article__body--right']//*[contains(text(), 'Create Account')]")

    sign_in_email_input = (By.XPATH, "//input[@id='email']")
    sign_in_password_input = (By.XPATH, "//input[@id='password']")
    access_denied_message = (By.XPATH, "//*[contains(text(), 'Access denied - wrong email address or password.')]")

    welcome_message = (By.XPATH, "//h1[contains(text(), 'Hi')]")

    sign_out_link = (By.ID, "my-out")



# Access denied - wrong email address or password.


class RegisterLocators:
    register_name = (By.XPATH, "//input[@name='fullname']")
    register_email = (By.XPATH, "//input[@name='email']")
    register_password = (By.XPATH, "//input[@name='password']")
    register_password1 = (By.XPATH, "//input[@name='password1']")

    create_account_button = (By.ID, "create")
    register_error_msg = (By.ID, "errormessage")

# The password must be entered and then repeated exactly.
