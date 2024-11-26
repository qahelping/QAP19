from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

URL = "https://www.youtube.com"


@pytest.fixture(scope="function")
def youtube(driver):
    driver.get(URL)
    yield driver


def test_find_element(youtube: WebDriver):
    # если элемент найден
    assert youtube.find_element(By.ID, "contents")


def test_find_elements(youtube: WebDriver):
    # если элементы найдены
    lst = youtube.find_elements(By.XPATH, "//ytd-guide-entry-renderer")
    assert len(lst) >= 0


def test_find_element_0(youtube: WebDriver):
    #  если элемент НЕ найден
    try:
        youtube.find_element(By.ID, "contents_base")
        assert True
    except NoSuchElementException:
        assert False


def test_find_elements_0(youtube: WebDriver):
    # если элементы НЕ найдены
    youtube.set_window_size(900, 800)
    lst = youtube.find_elements(By.XPATH, "//ytd-guide-entry-renderer")
    assert lst == []


def test_text(youtube: WebDriver):
    # получить текст
    element = youtube.find_elements(By.CSS_SELECTOR, '[id="subtitle"]')[0]
    assert (
            element.text
            == "Start watching videos to help us build a feed of videos you'll love."
    )


@pytest.mark.only
def test_attribute(youtube: WebDriver):  # получить attribute
    element = youtube.find_elements(By.CSS_SELECTOR, '[id="subtitle"]')[0]
    class_of_elements = element.get_attribute("class")
    assert "ytd-feed-nudge-renderer" in class_of_elements


@pytest.mark.only
def test_find_value_of_css_property(youtube: WebDriver):
    element = youtube.find_elements(By.CSS_SELECTOR, '[id="subtitle"]')[0]
    css = element.value_of_css_property("font-weight")
    assert css == 400


@pytest.mark.skip
def test_find_element_without_fixture():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    assert driver.find_element(By.ID, "contents")
