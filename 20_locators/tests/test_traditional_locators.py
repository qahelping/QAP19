import time

import allure
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By

URL = 'https://www.canva.com/en_gb/'


@pytest.fixture()
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


@allure.epic("QAP 19")
@allure.feature("Lesson 20")
@allure.story("Selenium locators")
class TestTraditionalLocators:

    def test_by_id(self, driver):
        driver.get(URL)

        element = driver.find_element(By.ID, 'root')
        assert element.is_displayed()

    def test_by_id_invalid(self, driver):
        driver.get(URL)

        element = driver.find_element(By.ID, 'root1')
        assert element.is_displayed()

    def test_by_name(self, driver):
        driver.get(URL)

        element = driver.find_element(By.NAME, 'slack-app-id')
        assert element.is_displayed()

    def test_by_partial_link_text_by_all(self, driver):
        driver.get(URL)

        element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Skip to main content')
        assert element.is_displayed()

    def test_by_partial_link_text_by_part(self, driver):
        driver.get(URL)

        element = driver.find_element(By.PARTIAL_LINK_TEXT, 'Skip to main')
        assert element.is_displayed()

    def test_by_tag_div(self, driver):
        driver.get(URL)

        elements = driver.find_elements(By.TAG_NAME, 'div')
        assert len(elements) > 0

    def test_by_class_name_lst(self, driver):
        driver.get(URL)

        elements = driver.find_elements(By.CLASS_NAME, 'N00Reg')
        assert len(elements) == 7

    def test_by_class_name(self, driver):
        driver.get(URL)

        elements = driver.find_elements(By.CLASS_NAME, '_07T50w')
        assert elements != []
        assert elements[0].is_displayed()
        assert len(elements) == 1

    def test_all_selenium_locators(self, driver):
        driver.get('https://www.wildberries.by/')
        element1 = driver.find_element(By.CLASS_NAME, 'simple-menu__currency')
        element2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Корзина')
        element3 = driver.find_element(By.ID, 'searchInput')
        element4 = driver.find_element(By.CLASS_NAME, 'nav-element__logo')

        time.sleep(10)
        assert element1.is_displayed()
        assert element2.is_displayed()
        assert element3.is_displayed()
        assert element4.is_displayed()
