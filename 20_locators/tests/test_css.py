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
    # options = FirefoxOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


@allure.epic("QAP 19")
@allure.feature("Lesson 20")
@allure.story("CSS")
class TestCSSLocators:

    @pytest.mark.xfail
    def test_by_css_class_invalid(self, driver):
        driver.get(URL)

        element = driver.find_element(By.CSS_SELECTOR,
                                      '_1QoxDw Qkd66A tYI0Vw o4TrkA YPTJew Qkd66A tYI0Vw lsXp_w cwOZMg zQlusQ uRvRjQ YOzphQ ZnA_CQ')
        assert element.is_displayed()

    def test_by_css_class(self, driver):
        driver.get(URL)
        time.sleep(10)
        element = driver.find_element(By.CSS_SELECTOR,
                                      '._1QoxDw.Qkd66A.tYI0Vw.o4TrkA.NT2yCg.Qkd66A.tYI0Vw.lsXp_w.cwOZMg.zQlusQ.uRvRjQ._9Ix54Q')
        assert element.is_displayed()

    def test_by_css_id(self, driver):
        driver.get(URL)

        element = driver.find_element(By.CSS_SELECTOR, '#root')
        assert element.is_displayed()

    def test_by_tags_attr_full(self, driver):
        driver.get(URL)

        element = driver.find_element(By.CSS_SELECTOR, 'a[href="https://www.canva.com/en_gb/"]')
        assert element.is_displayed()

    def test_by_attr1(self, driver):
        driver.get(URL)

        element = driver.find_element(By.CSS_SELECTOR, '[href="https://www.canva.com/en_gb/"]')
        assert element.is_displayed()

    def test_by_attr2(self, driver):
        driver.get(URL)

        element = driver.find_element(By.CSS_SELECTOR, '[style="--NZu1Zw:24px"]')
        assert element.is_displayed()

    def test_by_class_attr_list(self, driver):
        driver.get(URL)

        elements = driver.find_elements(By.CSS_SELECTOR, '[class="eAUiHA"]')
        assert len(elements) == 5

    def test_by_id_css(self, driver):
        driver.get(URL)

        element = driver.find_element(By.CSS_SELECTOR, '[id=":R7gsb:0"]d')
        assert element.is_enabled()

    def test_by_css_combination(self, driver):
        driver.get(URL)

        elements = driver.find_elements(By.CLASS_NAME, 'p > a[class="ovm4pQ qN_0PQ"]')
        assert len(elements) == 7

    def test_by_part_class(self, driver):
        driver.get(URL)

        elements = driver.find_elements(By.CLASS_NAME, '[href^="https://static.canva.com"]')
        assert len(elements) > 0

    URL = 'https://www.wildberries.by/'

    def test_by_css_tags_start_of_the_str(self, driver):
        driver.get(URL)
        element = driver.find_element(By.CSS_SELECTOR, 'a[href^="https"]')
        assert element.is_displayed()

    def test_by_css_tags_sub_str(self, driver):
        driver.get(URL)
        element = driver.find_element(By.CSS_SELECTOR, 'a[href*="https"]')
        assert element.is_displayed()

    def test_by_css_parents(self, driver):
        driver.get(URL)
        element = driver.find_element(By.CSS_SELECTOR, '[class="header"] [class="header__wrapper"]')
        assert element.is_displayed()
