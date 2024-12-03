import pytest
from playwright.sync_api import Page, expect

url = "https://demo.playwright.dev/todomvc/#/"

def test_open_page(page: Page):
    page.goto(url)

    locator = page.locator('css=[class="header"]')
    locator = page.locator('xpath=//*[@class="header"]')
    locator = page.locator('//*[@class="header"]')
    page.screenshot(path="page.png")
    page.screenshot(path="page_full.png", full_page=True)
    locator.screenshot(path="page_locator.png")
    breakpoint()
    locator.wait_for()
    locator.click()


    expect(locator).to_be_visible()
    expect(page).to_have_title("React • TodoMVC")
    expect(page).to_have_url(url)

url = "https://playwright.dev/python/docs/trace-viewer"

def test_open_page_full(page: Page):
    page.goto(url)

    page.screenshot(path="page_full.png", full_page=True)

    expect(page).to_have_url(url)
