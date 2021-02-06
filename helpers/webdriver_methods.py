from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def move_to_and_click(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).pause(1).click().perform()

def send_keys(driver, element, *keys):
    element.click()
    element.clear()
    element.send_keys(keys)
