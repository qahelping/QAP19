import time

import allure
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
@allure.story("XPATH")
class TestXpath:

    def test_by_xpath(self, driver):
        driver.get(URL)
        time.sleep(10)
        element = driver.find_element(By.XPATH, '/html/body/div[1]')
        assert element.is_displayed()

    @allure.title("Element '/html/body/div[90]' is not displayed")
    @pytest.mark.xfail
    def test_by_xpath_class_invalid(self, driver):
        driver.get(URL)

        try:
            element = driver.find_element(By.XPATH, '/html/body/div[90]')
            assert element.is_displayed()
        except NoSuchElementException:
            assert False, 'Element not found'

    @allure.title("Element with is displayed")
    @allure.description(
        "This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
    @allure.tag("xpath")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.label("owner", "Helen Yanushevskaya")
    @allure.link(URL, name="Canva")
    @allure.issue("Lesson 20")
    @allure.testcase("TMS-456")
    def test_by_xpath_class_with(self, driver):
        driver.get(URL)
        time.sleep(10)
        element = driver.find_element(By.XPATH,
                                      '//button[@class="_1QoxDw Qkd66A tYI0Vw o4TrkA NT2yCg Qkd66A tYI0Vw lsXp_w cwOZMg zQlusQ uRvRjQ _9Ix54Q"]')
        assert element.is_displayed()

    def test_by_xpath_class(self, driver):
        driver.get(URL)
        time.sleep(10)
        element = driver.find_element(By.XPATH,
                                      '//*[@class="_1QoxDw Qkd66A tYI0Vw o4TrkA NT2yCg Qkd66A tYI0Vw lsXp_w cwOZMg zQlusQ uRvRjQ _9Ix54Q"]')
        assert element.is_displayed()

    def test_by_xpath_tag(self, driver):
        driver.get(URL)

        element = driver.find_element(By.XPATH, '//body')
        assert element.is_displayed()

    def test_by_xpath_all(self, driver):
        driver.get(URL)

        element = driver.find_element(By.XPATH, '//*')
        assert element.is_displayed()

    def test_by_xpath_id(self, driver):
        driver.get(URL)

        element = driver.find_element(By.XPATH, '//*[@id="root"]')
        assert element.is_displayed()

    def test_by_tags_attr_full(self, driver):
        driver.get(URL)

        element = driver.find_element(By.XPATH, '//a[@href="https://www.canva.com/en_gb/"]')
        assert element.is_displayed()

    def test_by_attr1(self, driver):
        driver.get(URL)

        element = driver.find_element(By.XPATH, '//div[@class="NoN2AA _5_MXiw"]//div[@class="jv5LaQ"]')
        assert element.is_displayed()

    def test_by_text(self, driver):
        driver.get(URL)

        element = driver.find_element(By.XPATH, '//*[text()="Accept all cookies"]')
        assert element.is_displayed()

    def test_by_part_text(self, driver):
        driver.get(URL)

        elements = driver.find_elements(By.XPATH, '//*[contains(text(),"ept all cook")]')
        assert len(elements) == 5

    def test_by_id_css(self, driver):
        driver.get(URL)

        element = driver.find_element(By.XPATH, '//*[contains(@class,"NoN2AA")]')
        assert element.is_enabled()

    def test_by_xpath_combination(self, driver):
        driver.get(URL)

        elements = driver.find_elements(By.CLASS_NAME, 'p > a[class="ovm4pQ qN_0PQ"]')
        assert len(elements) == 7

    def test_by_part_class(self, driver):
        driver.get(URL)

        elements = driver.find_elements(By.CLASS_NAME, '[href^="https://static.canva.com"]')
        assert len(elements) > 0

    # URL = 'https://www.wildberries.by/'
    #
    # def test_by_xpath_tags_start_of_the_str(self, driver):
    #     driver.get(URL)
    #     element = driver.find_element(By.XPATH, 'a[href^="https"]')
    #     assert element.is_displayed()
    #
    #
    # def test_by_xpath_tags_sub_str(self, driver):
    #     driver.get(URL)
    #     element = driver.find_element(By.XPATH, 'a[href*="https"]')
    #     assert element.is_displayed()
    #
    # def test_by_xpath_parents(self, driver):
    #     driver.get(URL)
    #     element = driver.find_element(By.XPATH, '[class="header"] [class="header__wrapper"]')
    #     assert element.is_displayed()

    def test_attach(self, driver):
        driver.get(URL)
        png_bytes = driver.save_screenshot('screenshot.png')
        allure.attach(
            png_bytes,
            name="full-page",
            attachment_type=allure.attachment_type.PNG
        )
