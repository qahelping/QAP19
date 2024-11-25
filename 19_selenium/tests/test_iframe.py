import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


def test_iframe(browser_practice_automation):
    selector = '[aria-label="Skip to main content"]'
    browser_practice_automation.get('https://practice-automation.com/iframes/')
    frame = browser_practice_automation.find_element(By.ID, "iframe-1")
    browser_practice_automation.switch_to.frame(frame)

    assert browser_practice_automation.find_element(By.CSS_SELECTOR, selector).is_displayed()

    browser_practice_automation.switch_to.default_content()