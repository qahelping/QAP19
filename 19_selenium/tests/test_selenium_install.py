from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as  FirefoxService


def test_firefox_install():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    url = "https://www.google.com/"
    driver.get(url)

    assert driver.current_url == url
    assert driver.title == "Google"

    driver.close()
    driver.quit()

def test_chrome_install():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://www.google.com/"
    driver.get(url)

    assert driver.current_url == url
    assert driver.title == "Google"

    driver.quit()

def test_firefox_install_fixture(driver):
    url = "https://www.google.com/"
    driver.get(url)

    assert driver.current_url == url
    assert driver.title == "Google"
