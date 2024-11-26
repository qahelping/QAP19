import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    @allure.step("Click on ${selector}")
    def click(self, selector: str, force=False):
        element = self.get_element(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        if force:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def alert_accept(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text

    def alert_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def prompt(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def fill(self, selector, text):
        element = self.get_element(*selector)
        element.send_keys(text)

    def get_element(self, selector):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(selector))
        return element

    def add_cookie(self, name, value):
        cookie = {'name': name, 'value': value}
        self.driver.add_cookie(cookie)

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)
        allure.attach('screenshot', self.driver.get_screenshot_as_png(), type=AttachmentType.PNG)

    #  selector = (By.ID, 'name')
    def get_text(self, selector):
        element = self.get_element(*selector)
        return element.text

    def open_page(self, url):
        self.driver.get(url)
