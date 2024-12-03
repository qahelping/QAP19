import re
from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://demo.playwright.dev/todomvc/#/")
#     page.get_by_placeholder("What needs to be done?").click()
#     page.get_by_placeholder("What needs to be done?").fill("hello")
#     page.get_by_placeholder("What needs to be done?").press("Enter")
#     page.get_by_label("Toggle Todo").check()
#     page.get_by_role("link", name="All").click()
#     page.get_by_role("link", name="Active").click()
#     page.get_by_role("link", name="Completed").click()
#     page.locator("html").click()
#     expect(page.get_by_label("Toggle Todo")).to_be_visible()
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").fill("hello")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_label("Toggle Todo").check()
    page.get_by_role("link", name="All").click()
    page.locator("html").click()
    expect(page.get_by_label("Toggle Todo")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()