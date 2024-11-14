import time
from pytest import mark
from selenium.webdriver.chrome.webdriver import WebDriver
from window_size import WINDOWS_SIZE

@mark.skip
def test_maximize_window(driver: WebDriver):
    driver.maximize_window()

    url = "https://www.google.com/"
    driver.get(url)
    time.sleep(10)
    assert driver.title == "Google"

@mark.skip
def test_minimize_window(driver: WebDriver):
    driver.minimize_window()

    url = "https://www.google.com/"
    driver.get(url)
    time.sleep(10)
    assert driver.title == "Google"


@mark.parametrize('a,b', WINDOWS_SIZE)
def test_set_window_size(driver: WebDriver, a, b):
    driver.set_window_size(width=a, height=b)
    url = "https://www.google.com/"
    driver.get(url)
    assert driver.title == "Google"


