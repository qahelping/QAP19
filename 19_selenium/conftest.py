import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as  FirefoxService


@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver

    driver.close()
    driver.quit()


@pytest.fixture(scope='function')
def youtube(driver):
    URL = 'https://www.youtube.com'
    driver.get(URL)
    yield driver


@pytest.fixture(scope='function')
def browser_practice_automation(driver):
    URL = 'https://practice-automation.com/form-fields/'
    driver.get(URL)
    yield driver


