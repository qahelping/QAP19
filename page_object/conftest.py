import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as  FirefoxService

from page_object.data import BASE_URL


@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver

    driver.close()
    driver.quit()


