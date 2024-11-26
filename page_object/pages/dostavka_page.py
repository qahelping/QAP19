import time

import allure
from selenium.webdriver.common.by import By

from page_object.core import BasePage
from page_object.data import BASE_URL


class DostavkaPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.path = f'{BASE_URL}/services/besplatnaya-dostavka?'


    @allure.step('Open "Dostavka" page')
    def open(self):
        self.open_page(self.path)

    @allure.step('Assert that "Dostavka" page is open')
    def assert_that_page_is_open(self):
        assert self.get_element((By.CSS_SELECTOR, 'div.delivery-banner'))
        self.save_screenshot('page_object/screenshots/assert_that_page_is_open.png')


