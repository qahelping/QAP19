from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By



def test_click(youtube: WebDriver): #  если элемент найден
    first_element = youtube.find_elements(By.XPATH, '//ytd-guide-entry-renderer')[0]
    first_element.click()
