import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def get_by_data_testid(selector):
    return f'[data-testid="{selector}"]'


def test_fill(browser_practice_automation: WebDriver):
    first_element = browser_practice_automation.find_element(By.CSS_SELECTOR, get_by_data_testid('name-input'))
    first_element.send_keys('Max')
    browser_practice_automation.save_screenshot('test_fill.png')


def test_fill_none(browser_practice_automation: WebDriver):
    first_element = browser_practice_automation.find_element(By.CSS_SELECTOR, get_by_data_testid('name-input'))
    first_element.send_keys('Max')
    first_element.send_keys('')
    browser_practice_automation.save_screenshot('test_fill_none.png')


def test_fill_clear(browser_practice_automation: WebDriver):
    first_element = browser_practice_automation.find_element(By.CSS_SELECTOR, get_by_data_testid('name-input'))
    first_element.send_keys('Max')
    first_element.clear()
    browser_practice_automation.save_screenshot('test_fill_clear.png')


def test_fill_for(browser_practice_automation: WebDriver):
    first_element = browser_practice_automation.find_element(By.CSS_SELECTOR, get_by_data_testid('name-input'))
    str = "my is Max"
    for i in str:
        first_element.send_keys(i)
    browser_practice_automation.save_screenshot('test_fill_for.png')



def test_get_text(browser_practice_automation: WebDriver):
    first_element = browser_practice_automation.find_element(By.CSS_SELECTOR, '[itemprop="headline"]')
    str = first_element.text
    assert str == 'Form Fields'

