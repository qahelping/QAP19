import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


def test_open_windows(browser_practice_automation):
    browser_practice_automation.get('https://practice-automation.com/window-operations/')
    curren_id = browser_practice_automation.current_window_handle

    assert len(browser_practice_automation.window_handles()) == 1
    browser_practice_automation.find_element(By.CSS_SELECTOR, "[onclick='newTab()']").click()
    assert browser_practice_automation.find_element(By.CSS_SELECTOR,
                                                    '[class="wp-block-heading"]').is_displayed()

    curren_id_after_opening = browser_practice_automation.current_window_handle

    assert len(browser_practice_automation.window_handles()) == 2
    assert curren_id == curren_id_after_opening

    print(browser_practice_automation.window_handles())

    browser_practice_automation.switch_to.window(browser_practice_automation.window_handles()[1])

    assert browser_practice_automation.current_window_handle != curren_id

    assert browser_practice_automation.find_element(By.CSS_SELECTOR, '[aria-label="Please allow ads on our site"]').is_displayed()


