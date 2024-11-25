import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def wait_for(driver, selector):
    locator = (By.CSS_SELECTOR, selector)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    )
    return element

def test_ec(browser_practice_automation):
    browser_practice_automation.get('https://the-internet.herokuapp.com/dynamic_loading/1')

    element = wait_for(browser_practice_automation, '#start')
    element.click()

    element_finish = wait_for(browser_practice_automation, '#finish')
    assert element_finish.is_enabled()



def test_find_element(browser_practice_automation):
    browser_practice_automation.get('https://the-internet.herokuapp.com/dynamic_loading/1')

    element = browser_practice_automation.find_element(By.CSS_SELECTOR, '#start')
    element.click()

    element_finish = browser_practice_automation.find_element(By.CSS_SELECTOR, '#finish')
    assert element_finish.is_enabled()