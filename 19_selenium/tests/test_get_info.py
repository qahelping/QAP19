from selenium.webdriver.chrome.webdriver import WebDriver
import pytest

URL = 'https://www.youtube.com'


@pytest.fixture(scope='function')
def youtube(driver):
    driver.get(URL)
    yield driver


def test_get_info(youtube: WebDriver):
    assert youtube.current_url == URL
    assert youtube.title == 'YouTube'
    assert youtube.page_source
