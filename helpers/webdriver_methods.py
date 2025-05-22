from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


def move_to_and_click(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element).pause(1).click().perform()


def send_keys(element, *keys):
    element.click()
    element.clear()
    element.send_keys(keys)


def wait_until_el_visible(driver, by, selector):
    return WebDriverWait(driver, 10).until(ec.visibility_of_element_located((by, selector)))


def force_click(driver, by, selector):
    element = WebDriverWait(driver, 5).until(
        ec.presence_of_element_located((by, selector))
    )
    driver.execute_script("arguments[0].click();", element)
