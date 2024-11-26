import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


def alert_accept(driver):
    alert = driver.switch_to.alert
    text = alert.text
    alert.accept()
    return text


def alert_dismiss(driver):
    alert = driver.switch_to.alert
    alert.dismiss()


def prompt(driver, text):
    alert = driver.switch_to.alert
    alert.send_keys(text)
    alert.accept()


def test_alert(browser_practice_automation):
    browser_practice_automation.get("https://practice-automation.com/popups/")
    browser_practice_automation.find_element(By.ID, "prompt").click()
    time.sleep(10)
    prompt(browser_practice_automation, "hello world")
