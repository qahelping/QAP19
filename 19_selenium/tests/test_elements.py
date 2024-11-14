import time

import pytest
from pytest import mark
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from window_size import WINDOWS_SIZE

URL = 'https://www.youtube.com'

@pytest.fixture(scope='function')
def youtube(driver):
    driver.get(URL)
    yield driver


def test_find_element(youtube: WebDriver):
    assert youtube.find_element(By.ID, 'contents')

