from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


def test_click(youtube: WebDriver):  #  если элемент найден
    first_element = youtube.find_elements(By.XPATH, "//ytd-guide-entry-renderer")[0]
    first_element.click()


def test_action(browser_practice_automation: WebDriver):
    action: ActionChains = ActionChains(browser_practice_automation)

    first_element = browser_practice_automation.find_element(
        By.CSS_SELECTOR, '[itemprop="headline"]'
    )
    action.double_click(first_element)
    action.perform()

    assert str == "Form Fields"


def test_js(browser_practice_automation):
    element = browser_practice_automation.find_element(
        By.CSS_SELECTOR, '[itemprop="headline"]'
    )
    browser_practice_automation.execute_script(
        "arguments[0].scrollIntoView();", element
    )
    browser_practice_automation.execute_script("arguments[0].click();", element)


def test_select1(browser_practice_automation):
    select = Select(browser_practice_automation)
    select.select_by_index(1)

    select.select_by_value("no")

    select.select_by_visible_text("Yes")


def test_select2(browser_practice_automation):
    select_element = browser_practice_automation.find_element(
        By.CSS_SELECTOR, '[data-testid="automation"]'
    )
    select_element.click()

    option = browser_practice_automation.find_element(
        By.CSS_SELECTOR, '[data-testid="automation-default"]'
    )
    option.click()


def click(driver: WebDriver, selector: str, force=False):
    element = driver.find_element(By.CSS_SELECTOR, selector)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    if force:
        driver.execute_script("arguments[0].click();", element)
    else:
        element.click()


def force_click(driver: WebDriver, selector: str):
    element = driver.find_elements(By.CSS_SELECTOR, selector)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)
